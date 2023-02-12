import numpy as np


def sem(data):
    '''standard error of the mean'''
    return np.std(data) / len(data)
