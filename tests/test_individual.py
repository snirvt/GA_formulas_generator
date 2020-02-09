import unittest   # The test framework'
from unittest.mock import MagicMock

import numpy as np

###################################
import individual    # The code to test
from individual import Individual
from probability_handler import Probability_Handler
###################################

class Test_Individual(unittest.TestCase):

    def test_init(self):
        num_features = 10
        max_individual_size = 5
        num_actions = 6 

        i = Individual(num_features = num_features, max_individual_size = max_individual_size, num_actions = num_actions)

        size_individual = i.individual_size
        self.assertTrue(1 <= size_individual <= max_individual_size)

        size_indices = len(i.feature_indices)
        self.assertTrue(1 <= size_indices <= max_individual_size)
        self.assertTrue(np.all(0 <= np.array(size_indices) <= num_features))

        size_tree_values = len(i.weights)
        self.assertTrue(1 <= size_tree_values <= max_individual_size)
        self.assertTrue(0 <= np.min(i.weights))
        self.assertTrue(np.max(i.weights) <= 1)

        # self.assertEqual(list(np.sort(i.tree_values)) , list(np.arange(size_individual)))

        size_parentheses_binary_vec = len(i.parentheses_binary_vec)
        self.assertTrue(1 <= size_parentheses_binary_vec <= max_individual_size)
        self.assertTrue(np.all(0 <= np.array(i.parentheses_binary_vec)))
        self.assertTrue(np.all(np.array(i.parentheses_binary_vec) <= 1))

        size_action_vector = len(i.actions)
        self.assertTrue(1 <= size_action_vector <= max_individual_size)
        self.assertTrue(np.all(0 <= np.array(i.parentheses_binary_vec)))
        self.assertTrue(np.all(np.array(i.parentheses_binary_vec) < num_actions))



    def test_add_genotype_parts(self):
        pass

if __name__ == '__main__':
    unittest.main()
