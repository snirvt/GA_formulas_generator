import numpy as np
import random

def generate_gaussian_integers(mu, sigma, lower_limit = 1, upper_limit = 5, size = 1):
    res = np.random.normal(mu, sigma, size)
    res[res < lower_limit] = lower_limit
    res[res > upper_limit] = upper_limit
    return res.astype(int)


def generate_n_unique_random_integers(n):
    res = list(range(n))
    random.shuffle(res)
    return res


def generate_n_uniform_random_values(n):
    res = np.random.rand(n)
    return list(res)


def generate_n_uniform_random_integers(min_val , max_val , size ):
    res = np.random.randint(min_val, max_val, size)
    return list(res)
