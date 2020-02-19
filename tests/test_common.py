
import numpy as np



def create_data():
    ## pattern is 0*1/2
    X = np.random.rand(100,3)
    y = X[:,0] * X[:,1] / X[:,2]
    column_names = [1,2,3]
    return X, y, column_names


def create_simple_individual():
    dna_dict = {}
    dna_dict['size'] = 3
    dna_dict['feature_indices'] = [0,1,2]
    dna_dict['weights'] = [0,1,2]
    dna_dict['parentheses_binary_vec'] = [0,0,0]
    dna_dict['actions'] = [2,3,2]
    return dna_dict









