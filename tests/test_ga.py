import numpy as np
import pytest
import mock

import unittest   # The test framework'
from unittest.mock import MagicMock

###################################
from ga import GA
from tests.test_common import create_data
###################################

class Test_ga(unittest.TestCase):
    def test_create_population(self):
        population_size = 10
        ga = create_ga_test(population_size = population_size)
        ga.create_population(population_size=population_size)
        self.assertEqual(len(ga.get_population()),  population_size)

    def test_mutate_population(self):
        population_size = 10
        ga = create_ga_test(population_size = population_size)
        ga.create_population(population_size = population_size)
        ga.mutate_population()
        self.assertEqual(len(ga.get_population()), population_size)


def create_ga_test(population_size = 10):
    X, X_test, y, y_test, column_names = create_data()
    ga = GA(X=X, X_test = X_test, y=y, y_test = y_test, column_names = column_names,output_path='test')
    return ga




