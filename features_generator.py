

import numbers_generator as ng
import constants

def create_size_feature(mu=3, sigma = 1, lower_limit=1, upper_limit=5):
    return ng.generate_gaussian_integers(mu=mu, sigma=sigma, lower_limit=lower_limit, upper_limit=upper_limit)[0]

def sample_size(mu):
    return ng.generate_gaussian_integers(mu=mu, sigma=1, lower_limit=1, upper_limit=constants.MAX_SIZE_INDIVIDUAL)[0]    

def create_feature_index_vector(num_features, size):
    return ng.generate_n_uniform_random_integers(min_val=0, max_val = num_features, size = size)

def sample_feature_index(num_features):
    return ng.generate_n_uniform_random_integers(min_val=0, max_val = num_features, size = 1)[0]

def create_weight_vector(size):
    return ng.generate_n_uniform_random_values(n = size)

def sample_weight():
    return ng.generate_n_uniform_random_values(n = 1)[0]

def create_parentheses_vector(size):
    return ng.generate_n_uniform_random_integers(0 , 2 , size)

def sample_parentheses():
    return create_parentheses_vector(1)[0]

def create_action_vector(size):
    return ng.generate_n_uniform_random_integers(min_val=0 , max_val = constants.NUM_ACTIONS ,size = size)

def sample_action():
    return ng.generate_n_uniform_random_integers(min_val=0 , max_val = constants.NUM_ACTIONS ,size = 1)[0]

def create_wl_scalars_vector(mu, sigma, size):
    return ng.generate_gaussian(mu=mu, sigma = sigma, size = size)

def sample_wl_scalars(mu, sigma):
    return ng.generate_gaussian(mu=mu, sigma = sigma, size = 1)[0]

def create_wl_powers_vector(mu, sigma, size):
    return ng.generate_gaussian(mu=mu, sigma = sigma, size = size)

def sample_wl_powers(mu, sigma):
    return ng.generate_gaussian(mu=mu, sigma = sigma, size = 1)[0]

def create_parentheses_bias_vector(mu, sigma, size):
    return ng.generate_gaussian(mu=mu, sigma = sigma, size = size)

def sample_parentheses_bias(mu, sigma):
    return ng.generate_gaussian(mu=mu, sigma = sigma, size = 1)[0]