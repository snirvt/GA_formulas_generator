
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







    