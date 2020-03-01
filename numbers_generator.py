import numpy as np
import random

def generate_gaussian_integers(mu, sigma, lower_limit = 1, upper_limit = 5, size = 1):
    res = np.random.normal(mu, sigma, size)
    res[res < lower_limit] = lower_limit
    res[res > upper_limit] = upper_limit
    return res.astype(int)

def generate_gaussian(mu, sigma, size):
    res = np.random.normal(mu, sigma, size)
    for i in range(len(res)):
        res[i] = round(res[i],2)
    return list(res)

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

def generate_n_binary_numbers(size):
    return generate_n_uniform_random_integers(0 , 2 , size)

def generate_non_uniform_integers(values,distribution_list, size):
    res =  np.random.choice(values ,size=size, p = distribution_list)  # [0.5, 0.1, 0.1, 0.1, 0.1, 0.1]
    return list(res)