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

        i = Individual(num_features = num_features, max_individual_size = max_individual_size, probability_handler=None, num_actions = num_actions)

        size_individual = i.individual_size
        self.assertTrue(1 <= size_individual <= max_individual_size)

        size_indices = len(i.feature_indices)
        self.assertTrue(1 <= size_indices <= max_individual_size)
        self.assertTrue(np.all(0 <= np.array(size_indices) <= num_features))

        size_tree_values = len(i.tree_values)
        self.assertTrue(1 <= size_tree_values <= max_individual_size)
        self.assertEqual(list(np.sort(i.tree_values)) , list(np.arange(size_individual)))

        size_parentheses_binary_vec = len(i.parentheses_binary_vec)
        self.assertTrue(1 <= size_tree_values <= max_individual_size)
        self.assertTrue(np.all(0 <= np.array(i.parentheses_binary_vec)))
        self.assertTrue(np.all(np.array(i.parentheses_binary_vec) <= 1))

        
        size_action_vector = len(i.action_vector)
        self.assertTrue(1 <= size_action_vector <= max_individual_size)
        self.assertTrue(np.all(0 <= np.array(i.parentheses_binary_vec)))
        self.assertTrue(np.all(np.array(i.parentheses_binary_vec) < num_actions))


    # def test_mutate(self):
    #     num_features = 10
    #     max_individual_size = 5
    #     probability_handler = Probability_Handler()
    #     i = Individual(num_features = num_features, max_individual_size = max_individual_size, probability_handler=probability_handler)
    #     self.assertTrue(i.mutate()==0.1)


    def test_remove_genotype_parts(self): # TODO - add mock to control the exact result
        num_features = 10
        max_individual_size = 5
        probability_handler = Probability_Handler()
        
        i = Individual(num_features = num_features, max_individual_size = max_individual_size, probability_handler=probability_handler)
        size_before = i.individual_size
        
        i.remove_genotype_parts(max_individual_size - 1)
        size_after = i.individual_size
        
        if size_before == 1:
            self.assertEqual(size_before , size_after)
        else: 
            self.assertEqual(size_before , size_after + 1)

if __name__ == '__main__':
    unittest.main()
