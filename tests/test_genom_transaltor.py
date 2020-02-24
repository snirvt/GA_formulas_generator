import unittest   # The test framework'
from unittest.mock import MagicMock
import numpy as np
import pytest
import mock

from tests.test_common import create_data, create_simple_individual, create_simple_population
from genom_transaltor import Genom_Translator
import constants

class Test_Genom_Transaltor(unittest.TestCase):
    def test_build_individual_binary_tree(self):
        dna_dict,pre_order_correct = create_dna_dict()
        genom_translator = Genom_Translator(column_names=None)
        genom_translator.build_individual_binary_tree(dna_dict)
        tree = genom_translator.tree
        self.assertIsNotNone(tree)
        pre_order_result = []
        tree.pre_order(pre_order_result)
        self.assertIsNotNone(pre_order_result)
        self.assertEqual(pre_order_result, pre_order_correct)
        genom_translator.build_individual_binary_tree(dna_dict) ## check if the first tree is deleted
        self.assertEqual(pre_order_result, pre_order_correct)

    def test_extract_tree_expression(self):
        dna_dict, _ = create_dna_dict()
        genom_translator = Genom_Translator(column_names=None)
        genom_translator.build_individual_binary_tree(dna_dict)
        tree = genom_translator.tree
        expression = genom_translator.extract_tree_expression(tree.node, index_mark = '_')
        self.assertIsNotNone(expression)
        self.assertEqual(expression, '((1*_1_)+(1*_3_)*(1*_5_)^((1*_2_)-((1*_4_))/(1*_6_)))+')

def create_dna_dict():
    dna_dict = {}
    dna_dict['size'] = 6
    dna_dict['feature_indices'] = [1,2,3,4,5,6]
    dna_dict['weights'] = [3,5,1,4,2,6]
    dna_dict['parentheses_binary_vec'] = [1,1,0,1,0,0]
    dna_dict['actions'] = [0,1,2,3,4,0]
    dna_dict['wl_scalar'] = [1,1,1,1,1,1]
    pre_order_correct = [(3, 1, 1, 0,1), (1, 3, 0, 2,1), (2, 5, 0, 4,1), (5, 2, 1, 1,1), (4, 4, 1, 3,1), (6, 6, 0, 0,1)]
    return dna_dict, pre_order_correct

@pytest.fixture(name="translator_handler")
def translator_fixture(mocker):
    #  Bring up
    _, _ , column_names = create_data()
    yield Genom_Translator(column_names=column_names)
    #  Tear Down

@pytest.mark.parametrize('before_fix, after_fix', [('X[:,1]+X[:,1]^2+', 'X[:,1]+X[:,1]**2')])
def test_fix_translation(before_fix,after_fix, translator_handler):
    output = translator_handler.fix_expression(before_fix)
    assert(output == after_fix)
