import numpy as np
import random

class Numbers_Generator():
    @staticmethod
    def generate_gaussian_integers(mu, sigma, lower_limit = 1, upper_limit = 5, size = 1):
        res = np.random.normal(mu, sigma, size)
        res[res < lower_limit] = lower_limit
        res[res > upper_limit] = upper_limit
        return res.astype(int)
    @staticmethod
    def generate_n_unique_random_integers(n):
        res = list(range(n))
        random.shuffle(res)
        return res
    @staticmethod
    def generate_n_uniform_random_integers(min_val , max_val , size ):
        res = np.random.randint(min_val, max_val, size)
        return list(res)
