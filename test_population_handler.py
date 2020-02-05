

import unittest   # The test framework'
import numpy as np

###################################
import population_handler    # The code to test
from population_handler import Population_Handler
from probability_handler import Probability_Handler
###################################

class Test_Population_Handler(unittest.TestCase):

    def test_create_individual(self):
        probability_handler = Probability_Handler()
        ph = Population_Handler(num_features = 10, probability_handler=probability_handler, max_individual_size = 10)
        ind = ph.create_individual()
        self.assertIsNotNone(ind)

    def test_create_population(self):
        max_individual_size = 10
        num_features = 10
        population_size = 10
        probability_handler = Probability_Handler()

        ph = Population_Handler(num_features = num_features,probability_handler=probability_handler, max_individual_size = max_individual_size)
        ph.create_population(population_size = population_size)
        self.assertIsNotNone(ph.population)
        self.assertEqual(len(ph.population), population_size)
    


if __name__ == '__main__':
    unittest.main()



