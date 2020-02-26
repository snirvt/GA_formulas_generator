

import unittest   # The test framework'
import numpy as np

###################################
import population_handler    # The code to test
from population_handler import Population_Handler
from probability_handler import Probability_Handler
###################################

class Test_Population_Handler(unittest.TestCase):

    def test_create_individual(self):
        ph = create_test_population_handler()
        ind = ph.create_individual()
        self.assertIsNotNone(ind)

    def test_create_population(self):
        population_size = 10
        ph = create_test_population_handler()
        ph.create_population(population_size = population_size)
        self.assertIsNotNone(ph.population)
        self.assertEqual(len(ph.population), population_size)


    def test_mutate_population(self):
        ph = create_test_population_handler()
        population_size = 10
        ph.create_population(population_size = population_size)
        ph.mutate_population()
        self.assertIsNotNone(ph.population)
        self.assertEqual(len(ph.population), population_size)

    # def test_mutate_population_paralal(self):
    #     ph = create_test_population_handler()
    #     population_size = 10
    #     ph.create_population(population_size = population_size)
    #     ph.mutate_population_paralal()
    #     self.assertIsNotNone(ph.population)
    #     self.assertEqual(len(ph.population), population_size)

def create_test_population_handler(max_individual_size = 10, num_features = 10):
    probability_handler = Probability_Handler(max_feature_number = 10)
    ph = Population_Handler(probability_handler=probability_handler, max_individual_size = max_individual_size)
    return ph


if __name__ == '__main__':
    unittest.main()



