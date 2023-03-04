import numpy as np


def z_scale(vals):
    result = np.array(vals) - np.array(vals).mean()
    return (result / np.std(result)).round(4)


def linear_scale(vals):
    vals = np.array(vals)
    vals -= vals.min()
    return (vals / vals.max()).round(4)
