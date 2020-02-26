
import numpy as np
import constants


def create_data():
    ## pattern is 0*1/2
    X = np.random.rand(100,3)
    y = X[:,0] * X[:,1] / X[:,2]
    column_names = [1,2,3]
    return X, y, column_names


def create_simple_individual():
    dna_dict = {}
    dna_dict[constants.DNA_SIZE_STR] = 3
    dna_dict[constants.DNA_FEATURES_STR] = [0,1,2]
    dna_dict[constants.DNA_WEIGHTS_STR] = [0,1,2]
    dna_dict[constants.DNA_PARENTHESES_STR] = [0,0,0]
    dna_dict[constants.DNA_ACTIONS_STR] = [2,3,2]
    dna_dict[constants.DNA_WL_SCALAR] = [1,1,1]
    dna_dict[constants.DNA_WL_POWER] = [1,1,1]
    dna_dict[constants.DNA_PARENTHESES_BIAS] = [0,0,0]
    dna_dict[constants.DNA_WL_ACTIVATION] = [0,0,0]
    dna_dict[constants.DNA_PARENTHESES_ACTIVATION] = [0,0,0]
    return dna_dict

def create_simple_population():
    population = []
    for _ in range(3):
        population.append(create_simple_individual())
    return population






