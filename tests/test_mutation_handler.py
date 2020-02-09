import numpy as np
import pytest
import mock


import unittest   # The test framework'
from unittest.mock import MagicMock

###################################
from mutation_handler import Mutation_Handler
import numbers_generator as ng
from probability_handler import Probability_Handler
###################################




class Test_mutation_handler(unittest.TestCase):
    

    def create_dna_dict(self):
        dna_dict = {}
        dna_dict['size'] = 3
        dna_dict['feature_indices'] = [0,1,2]
        dna_dict['weights'] = [0,0.1,0.2]
        dna_dict['parentheses_binary_vec'] = [0,1,1]
        dna_dict['actions'] = [0,1,2]
        return dna_dict

    def test_remove_genotype_parts(self):
        mh = Mutation_Handler(probability_handler=None)
        dna_dict = self.create_dna_dict()
        mh.remove_genotype_parts(2,dna_dict)
        self.assertTrue(dna_dict['size'] == 2)
        self.assertTrue(len(dna_dict['feature_indices']) == 2)
        self.assertTrue(len(dna_dict['weights']) == 2)
        self.assertTrue(len(dna_dict['parentheses_binary_vec']) == 2)
        self.assertTrue(len(dna_dict['actions']) == 2)


    def test_add_genotype_parts(self):
        mh = Mutation_Handler(probability_handler=None)
        dna_dict = self.create_dna_dict()
        new_size = 5
        mh.add_genotype_parts(new_size,dna_dict)
        self.assertTrue(dna_dict['size'] == new_size)
        self.assertTrue(len(dna_dict['feature_indices']) == new_size)
        self.assertTrue(len(dna_dict['weights']) == new_size)
        self.assertTrue(len(dna_dict['parentheses_binary_vec']) == new_size)
        self.assertTrue(len(dna_dict['actions']) == new_size)



    def test_insert_new_values_to_dna(self):
        mh = Mutation_Handler(probability_handler=None)
        dna_dict = self.create_dna_dict()
        new_size = 4
        mh.insert_new_values_to_dna(0,dna_dict)
        self.assertTrue(dna_dict['size'] == new_size)
        self.assertTrue(len(dna_dict['feature_indices']) == new_size)
        self.assertTrue(len(dna_dict['weights']) == new_size)
        self.assertTrue(len(dna_dict['parentheses_binary_vec']) == new_size)
        self.assertTrue(len(dna_dict['actions']) == new_size)


    def test_vector_mutation(self):
        mh = Mutation_Handler(probability_handler=None)
        binary_list = [0,0,0]
        mh.vector_mutation(binary_list, 1, lambda : ng.generate_n_uniform_random_integers(min_val=1 , max_val=2 , size=1)[0])
        self.assertEqual(binary_list, [1,1,1])

    def test_apply_vector_mutation(self):
        mh = Mutation_Handler(probability_handler=Probability_Handler())
        dna_dict = self.create_dna_dict()
        mh.apply_vector_mutation(dna_dict['weights'], 'weights')
        self.assertEqual(len(dna_dict['weights']), 3)


    def test_mutate(self):
        mh = Mutation_Handler(probability_handler=Probability_Handler())
        dna_dict = self.create_dna_dict()
        mh.mutate(dna_dict)
        self.assertIsNotNone(dna_dict)


# @pytest.fixture(name="mut_handler")
# def mutation_handler_fixture(mocker):
#     #  Bring up
#     yield Mutation_Handler()
#     #  Tear Down


# @pytest.fixture(name="dna_dict")
# def dict_fixture(mocker):
#     #  Bring up
#     dna_dict = {}
#     dna_dict['size'] = 3
#     dna_dict['feature_indices'] = [0,1,2]
#     dna_dict['weights'] = [0,1,2]
#     dna_dict['parentheses_binary_vec'] = [0,1,1]
#     dna_dict['actions'] = [0,1,2]

#     yield dna_dict
#     #  Tear Down
 
# @pytest.mark.parametrize('dna_dict_size', [5,6])
# @pytest.mark.parametrize("gaus_int", [[5], [7]])
# @mock.patch("mutation_handler.ng", autospec=True)
# def test_mutate_size(mocked_ng, gaus_int, dna_dict_size, mut_handler, mocker):
#     mocked_ng.generate_gaussian_integers.return_value = gaus_int
#     mut_handler.remove_genotype_parts = mocker.MagicMock()
#     mut_handler.add_genotype_parts = mocker.MagicMock()
#     mut_handler.mutate_size({"size": dna_dict_size})
    

# @pytest.mark.parametrize("uniform_int", [[1]])
# @mock.patch("mutation_handler.ng", autospec=True)
# def test_remove_genotype_parts(mocked_ng, uniform_int, dna_dict, mut_handler, mocker):
    # mocked_ng.generate_n_uniform_random_integers.return_value = uniform_int
    # mut_handler.remove_genotype_parts = mocker.MagicMock()
    # mut_handler.add_genotype_parts = mocker.MagicMock()
    # mut_handler.remove_genotype_parts(2,dna_dict)
    # assert (dna_dict['size'] == 3)