import unittest   # The test framework'
from unittest.mock import MagicMock

import numpy as np

###################################
import individual    # The code to test
from individual import Individual
from probability_handler import Probability_Handler
import constants
###################################

class Test_Individual(unittest.TestCase):

    def test_be_born(self):
        num_features = 10
        max_individual_size = 5
        num_actions = 6 

        factory = Individual(num_features = num_features, max_individual_size = max_individual_size, num_actions = num_actions)
        dna_dict = factory.be_born()

        size_individual = dna_dict[constants.DNA_SIZE_STR]
        self.assertTrue(1 <= size_individual <= max_individual_size)

        size_indices = len(dna_dict[constants.DNA_FEATURES_STR])
        self.assertTrue(1 <= size_indices <= max_individual_size)
        self.assertTrue(np.all(0 <= np.array(size_indices) <= num_features))

        size_tree_values = len(dna_dict[constants.DNA_WEIGHTS_STR])
        self.assertTrue(1 <= size_tree_values <= max_individual_size)
        self.assertTrue(0 <= np.min(dna_dict[constants.DNA_WEIGHTS_STR]))
        self.assertTrue(np.max(dna_dict[constants.DNA_WEIGHTS_STR]) <= 1)

        size_parentheses_binary_vec = len(dna_dict[constants.DNA_PARENTHESES_STR])
        self.assertTrue(1 <= size_parentheses_binary_vec <= max_individual_size)
        self.assertTrue(np.all(0 <= np.array(dna_dict[constants.DNA_PARENTHESES_STR])))
        self.assertTrue(np.all(np.array(dna_dict[constants.DNA_PARENTHESES_STR]) <= 1))

        size_action_vector = len(dna_dict[constants.DNA_ACTIONS_STR])
        self.assertTrue(1 <= size_action_vector <= max_individual_size)
        self.assertTrue(np.all(0 <= np.array(dna_dict[constants.DNA_ACTIONS_STR])))
        self.assertTrue(np.all(np.array(dna_dict[constants.DNA_ACTIONS_STR]) < num_actions))


if __name__ == '__main__':
    unittest.main()
