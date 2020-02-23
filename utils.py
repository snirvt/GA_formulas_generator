
import numpy as np
import random

def activation():  # sin cos exp...
    pass


def swap_binary_value(binary_val):
    return 1 - binary_val

def r2_score(y_true, y_pred):
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