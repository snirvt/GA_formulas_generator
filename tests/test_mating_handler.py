
import numpy as np
import pytest
import mock

import unittest   # The test framework'
from unittest.mock import MagicMock

###################################
from mating_handler import Mating_Handler


@pytest.fixture(name="mate_handler")
def mating_fixture(mocker):
    #  Bring up
    yield Mating_Handler(num_offsprings_per_parent = 2)
    #  Tear Down

@pytest.mark.parametrize('population', [np.array(['e','c','b','a','d','f'])])
@pytest.mark.parametrize('fittness', [np.array([5,3,2,1,4,6])])
def test_sort_by_fitness(population, fittness, mate_handler):
    reversed_sorted = mate_handler.sort_by_fitness(population = population, population_fitness = fittness)
    assert(np.all(reversed_sorted == np.array(['a', 'b', 'c', 'd', 'e', 'f'])))

@pytest.mark.parametrize('population', [np.array(['e','c','b','a','h','d','g','f'])])
@pytest.mark.parametrize('fittness', [np.array([5,3,2,1,8,4,7,6])])
def test_choose_parents(population, fittness, mate_handler):
    sorted_population, num_parents = mate_handler.choose_parents(population = population, population_fitness = fittness)
    assert(num_parents == 4)
    assert(np.all(sorted_population[:2] == np.array(['a', 'b']))) ## check for num_parents/2 best individuals are parents

