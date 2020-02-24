import pytest
import mock
import unittest   # The test framework
import numpy as np

import numbers_generator as ng


class Test_Number_Generator(unittest.TestCase):

    ## generate_gaussian_integers_len
    def test_generate_gaussian_integers_len(self):
        num_1 = ng.generate_gaussian_integers(mu=3, sigma=1, lower_limit = 1, upper_limit = 5, size = 1)
        self.assertEqual(len(num_1), 1)
        self.assertEqual(num_1[0], int(num_1[0]))

        vec_1 = ng.generate_gaussian_integers(mu=3, sigma=1, lower_limit = 1, upper_limit = 5, size = 10)
        self.assertEqual(len(vec_1), 10)

    def test_generate_gaussian_integers_zero_sigma(self):
        num_1 = ng.generate_gaussian_integers(mu=3, sigma=0, lower_limit = 1, upper_limit = 5, size = 1)
        self.assertEqual(num_1, 3)

    def test_generate_gaussian_integers_values_limit(self):
        vec_1 = ng.generate_gaussian_integers(mu=3, sigma=1, lower_limit = 1, upper_limit = 5, size = 100)
        self.assertEqual(len(vec_1[vec_1<1]) , 0)
        self.assertEqual(len(vec_1[vec_1>5]) , 0)
    
    ## generate_n_unique_random_integers
    def test_generate_n_unique_random_integers(self):
        vec_1 = ng.generate_n_unique_random_integers(10)
        self.assertEqual(list(np.sort(vec_1)) , list(np.arange(10)))

    ## generate_n_uniform_random_integers
    def test_generate_n_uniform_random_integers(self):
        vec_1 = ng.generate_n_uniform_random_integers(min_val=0 , max_val=10 , size=10)
        vec_1 = np.array(vec_1)
        self.assertEqual(len(vec_1), 10)
        self.assertTrue(np.all(vec_1>=0))
        self.assertTrue(np.all(vec_1<10))

@pytest.mark.parametrize('size', [1, 25])
def test_generate_binary_values(size):
    result = ng.generate_n_binary_numbers(size = size)
    assert(len(result) == size)
    assert(check_if_binary(result))

@pytest.mark.parametrize('mu', [1])
@pytest.mark.parametrize('sigma', [0.5])
@pytest.mark.parametrize('size', [1, 25])
def test_generate_gaussian(mu, sigma, size):
    result = ng.generate_gaussian(mu=mu, sigma=sigma, size = size)
    assert(len(result) == size)

def check_if_binary(iterator):
    for value in iterator:
        if value != 0 and value != 1:
            return False
    return True