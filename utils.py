
import numpy as np
import random
from numpy import inf


def swap_binary_value(binary_val):
    return 1 - binary_val

def r2_score(y_true, y_pred):
    if len(y_pred[y_pred == -inf]) > 0 or len(y_pred[y_pred == inf]) > 0:
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    y_pred[y_pred == -inf] = 0
    y_pred[y_pred == inf] = 0
    SS_reg = np.sum((y_pred - y_true)**2)
    SS_tot = np.sum((np.mean(y_true) - y_true)**2)
    return 1 - SS_reg/SS_tot

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









    