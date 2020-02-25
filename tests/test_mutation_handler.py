import numpy as np
import pytest
import mock


import unittest   # The test framework'
from unittest.mock import MagicMock

###################################
from mutation_handler import Mutation_Handler
import numbers_generator as ng
from probability_handler import Probability_Handler
from tests.test_common import create_simple_individual
import constants
###################################

class Test_mutation_handler(unittest.TestCase):
    


    def test_remove_genotype_parts(self):
        mh = create_mutation_handler_test()
        dna_dict = create_simple_individual()
        mh.remove_genotype_parts(2,dna_dict)
        self.assertTrue(dna_dict[constants.DNA_SIZE_STR] == 2)
        self.assertTrue(len(dna_dict[constants.DNA_FEATURES_STR]) == 2)
        self.assertTrue(len(dna_dict[constants.DNA_WEIGHTS_STR]) == 2)
        self.assertTrue(len(dna_dict[constants.DNA_ACTIONS_STR]) == 2)
        self.assertTrue(len(dna_dict[constants.DNA_PARENTHESES_STR]) == 2)
        self.assertTrue(len(dna_dict[constants.DNA_WL_SCALAR]) == 2)


    def test_add_genotype_parts(self):
        mh = create_mutation_handler_test()
        dna_dict = create_simple_individual()
        new_size = 5
        mh.add_genotype_parts(new_size,dna_dict)
        self.assertTrue(dna_dict[constants.DNA_SIZE_STR] == new_size)
        self.assertTrue(len(dna_dict[constants.DNA_FEATURES_STR]) == new_size)
        self.assertTrue(len(dna_dict[constants.DNA_WEIGHTS_STR]) == new_size)
        self.assertTrue(len(dna_dict[constants.DNA_PARENTHESES_STR]) == new_size)
        self.assertTrue(len(dna_dict[constants.DNA_ACTIONS_STR]) == new_size)

    def test_insert_new_values_to_dna(self):
        mh = create_mutation_handler_test()
        dna_dict = create_simple_individual()
        new_size = 4
        mh.insert_new_values_to_dna(0,dna_dict)
        self.assertTrue(dna_dict[constants.DNA_SIZE_STR] == new_size)
        self.assertTrue(len(dna_dict[constants.DNA_FEATURES_STR]) == new_size)
        self.assertTrue(len(dna_dict[constants.DNA_WEIGHTS_STR]) == new_size)
        self.assertTrue(len(dna_dict[constants.DNA_PARENTHESES_STR]) == new_size)
        self.assertTrue(len(dna_dict[constants.DNA_ACTIONS_STR]) == new_size)

    def test_vector_mutation(self):
        mh = create_mutation_handler_test()
        binary_list = [0,0,0]
        mh.vector_mutation(binary_list, 1, lambda : ng.generate_n_uniform_random_integers(min_val=1 , max_val=2 , size=1)[0])
        self.assertEqual(binary_list, [1,1,1])

    def test_apply_vector_mutation(self):
        mh = create_mutation_handler_test()
        dna_dict = create_simple_individual()
        mh.apply_vector_mutation(dna_dict[constants.DNA_WEIGHTS_STR], constants.DNA_WEIGHTS_STR)
        self.assertEqual(len(dna_dict[constants.DNA_WEIGHTS_STR]), 3)

    def test_mutate(self):
        mh = create_mutation_handler_test()
        dna_dict = create_simple_individual()
        mh.mutate(dna_dict)
        self.assertIsNotNone(dna_dict)

def create_mutation_handler_test():
    probability_handler=Probability_Handler(max_feature_number=10)
    probability_handler.create_uniform_probability()
    mh = Mutation_Handler(probability_handler=probability_handler)
    return mh


@pytest.fixture(name="mut_handler")
def mutation_handler_fixture(mocker):
    #  Bring up
    yield Mutation_Handler(probability_handler=None)
    #  Tear Down


@pytest.fixture(name="dna_dict")
def dict_fixture(mocker):
    #  Bring up
    dna_dict = {}
    dna_dict[constants.DNA_SIZE_STR] = 3
    dna_dict[constants.DNA_FEATURES_STR] = [0,1,2]
    dna_dict[constants.DNA_WEIGHTS_STR] = [0,1,2]
    dna_dict[constants.DNA_PARENTHESES_STR] = [0,1,1]
    dna_dict[constants.DNA_ACTIONS_STR] = [0,1,2]

    yield dna_dict
    #  Tear Down
 
@pytest.mark.parametrize('dna_dict_size', [5,6])
@pytest.mark.parametrize("gaus_int", [5, 7])
@mock.patch("mutation_handler.fg", autospec=True)
def test_mutate_size(mocked_fg, gaus_int, dna_dict_size, mut_handler, mocker):
    mocked_fg.sample_size.return_value = gaus_int
    mut_handler.remove_genotype_parts = mocker.MagicMock(return_value=None)
    mut_handler.add_genotype_parts = mocker.MagicMock(return_value=None)
    mut_handler.mutate_size({constants.DNA_SIZE_STR: dna_dict_size})
    
    add_called = 0 ## how many times should the method be called
    remove_called = 0

    if (gaus_int < dna_dict_size):
        remove_called = 1

    if (gaus_int > dna_dict_size):
        add_called = 1

    assert(mut_handler.add_genotype_parts.call_count == add_called)
    assert(mut_handler.remove_genotype_parts.call_count == remove_called)
        
        

# @pytest.mark.parametrize("uniform_int", [[1]])
# @mock.patch("mutation_handler.ng", autospec=True)
# def test_remove_genotype_parts(mocked_ng, uniform_int, dna_dict, mut_handler, mocker):
    # mocked_ng.generate_n_uniform_random_integers.return_value = uniform_int
    # mut_handler.remove_genotype_parts = mocker.MagicMock()
    # mut_handler.add_genotype_parts = mocker.MagicMock()
    # mut_handler.remove_genotype_parts(2,dna_dict)
    # assert (dna_dict[constants.DNA_SIZE_STR] == 3)