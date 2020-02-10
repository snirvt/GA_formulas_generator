

import numpy as np
import pytest
import mock

import unittest   # The test framework'
from unittest.mock import MagicMock

###################################
from evaluator import Evaluator
###################################

class Test_Evaluator(unittest.TestCase):

    def test_create_population(self):
        dna_dict,pre_order_correct = create_dna_dict()
        evaluator = Evaluator(X=None,y=None, column_names=None)
        tree = evaluator.create_individual_binary_tree(dna_dict)
        self.assertIsNotNone(tree)

        pre_order_result = []
        tree.pre_order(pre_order_result)
        self.assertIsNotNone(pre_order_result)
        self.assertEqual(pre_order_result, pre_order_correct)





def create_dna_dict():
    dna_dict = {}
    dna_dict['size'] = 6
    dna_dict['feature_indices'] = [0,1,2,3,4,5]
    dna_dict['weights'] = [3,5,1,4,2,6]
    dna_dict['parentheses_binary_vec'] = [1,1,0,1,0,0]
    dna_dict['actions'] = [0,1,2,3,4,0]

    pre_order_correct = [(3, 0, 1, 0), (1, 2, 0, 2), (2, 4, 0, 4), (5, 1, 1, 1), (4, 3, 1, 3), (6, 5, 0, 0)]
    return dna_dict, pre_order_correct