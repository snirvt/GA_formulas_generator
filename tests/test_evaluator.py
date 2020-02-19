

import numpy as np
import pytest
import mock

import unittest   # The test framework'
from unittest.mock import MagicMock

###################################
from evaluator import Evaluator
from tests.test_common import create_data, create_simple_individual
###################################

class Test_Evaluator(unittest.TestCase):

    def test_build_individual_binary_tree(self):
        dna_dict,pre_order_correct = create_dna_dict()
        evaluator = Evaluator(X=None, y=None, column_names=None)
        evaluator.build_individual_binary_tree(dna_dict)
        tree = evaluator.tree
        self.assertIsNotNone(tree)
        pre_order_result = []
        tree.pre_order(pre_order_result)
        self.assertIsNotNone(pre_order_result)
        self.assertEqual(pre_order_result, pre_order_correct)
        evaluator.build_individual_binary_tree(dna_dict) ## check if the first tree is deleted
        self.assertEqual(pre_order_result, pre_order_correct)


    def test_extract_tree_expression(self):
        dna_dict, _ = create_dna_dict()
        evaluator = Evaluator(X=None, y=None, column_names=None)
        evaluator.build_individual_binary_tree(dna_dict)
        tree = evaluator.tree
        expression = evaluator.extract_tree_expression(tree.node, index_mark = '_')
        self.assertIsNotNone(expression)
        self.assertEqual(expression, '(_1_+_3_*_5_**(_2_-(_4_)/_6_))+')
        

def create_dna_dict():
    dna_dict = {}
    dna_dict['size'] = 6
    dna_dict['feature_indices'] = [1,2,3,4,5,6]
    dna_dict['weights'] = [3,5,1,4,2,6]
    dna_dict['parentheses_binary_vec'] = [1,1,0,1,0,0]
    dna_dict['actions'] = [0,1,2,3,4,0]

    pre_order_correct = [(3, 1, 1, 0), (1, 3, 0, 2), (2, 5, 0, 4), (5, 2, 1, 1), (4, 4, 1, 3), (6, 6, 0, 0)]
    return dna_dict, pre_order_correct



@pytest.fixture(name="eval_handler")
def evaluator_fixture(mocker):
    #  Bring up
    X, y , column_names = create_data()
    yield Evaluator(X=X, y=y, column_names=column_names)
    #  Tear Down

@pytest.mark.parametrize('input_num', [-1, 0, 1, 10])
def test_get_string_data_column(input_num, eval_handler):
    output = eval_handler.get_string_data_column(input_num)
    assert(output == 'X[:,{}]'.format(input_num))


@pytest.mark.parametrize('input_str', ['(_1_+_3_*_5_**(_2_-(_4_)/_6_))'])
def test_build_math_evaluation(input_str, eval_handler):
    output = eval_handler.build_math_evaluation(input_str)
    assert(output == '(X[:,1]+X[:,3]*X[:,5]**(X[:,2]-(X[:,4])/X[:,6]))')


def test_evaluate_individual(eval_handler):
    individual = create_simple_individual()
    output = eval_handler.evaluate_individual(individual)
    assert(output == 1)




