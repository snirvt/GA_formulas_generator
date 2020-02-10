

import numpy as np
import pytest
import mock


import unittest   # The test framework'
from unittest.mock import MagicMock

###################################
from tree import Tree_Node, Tree
###################################

class Test_tree(unittest.TestCase):
    
    def test_pre_order(self):
        data,pre_order_correct = create_tree_data()
        pre_order_result = []
        tree = Tree()
        for d in data:
            tree.insert(d)
        tree.pre_order(pre_order_result)
        self.assertEqual(pre_order_result, pre_order_correct)

        

def create_tree_data():
    data = [[3],[5],[1],[4], [2], [6]]
    pre_order_correct = [[3],[1],[2],[5], [4], [6]]
    return data, pre_order_correct



