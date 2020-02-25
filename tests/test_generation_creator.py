

import numpy as np
import pytest
import mock

import unittest   # The test framework'
from unittest.mock import MagicMock

###################################
from generation_creator import Generation_Creator
###################################

@pytest.fixture(name="generation_handler")
def mating_fixture(mocker):
    #  Bring up
    yield Generation_Creator()
    #  Tear Down

@pytest.mark.parametrize('parents_front', [np.array(['g','f','b','e','a','c','d','f'])])
@pytest.mark.parametrize('num_parents', [4])
def test_replicate_parents(parents_front, num_parents, generation_handler):
    replicated_parents = generation_handler.replicate_parents(parents_front = parents_front, num_parents = num_parents)
    assert(np.all(replicated_parents == np.array(['g', 'f', 'b', 'e', 'g', 'f', 'b', 'e'])))