
import numpy as np
import random
from numpy import inf


def swap_binary_value(binary_val):
    return 1 - binary_val

def scale(m):
    return (m-np.mean(m))/np.std(m)
    

def get_action(action):
    switcher = {
        0:'+',
        1:'-',
        2:'*',
        3:'/',
        4:'^',
    }
    return switcher.get(int(action))

def get_activation(activation):  # sin cos exp...
    switcher = {
        0:'', #identity
        1:'exp',
        2:'cos',
        3:'sin',
        4: 'absln',
    }
    return switcher.get(int(activation))



def snv(input_data):
    # Define a new array and populate it with the corrected data  
    data_snv = np.zeros_like(input_data)
    for i in range(input_data.shape[0]):
        # Apply correction
        data_snv[i,:] = (input_data[i,:] - np.mean(input_data[i,:])) / np.std(input_data[i,:])
    return data_snv



    