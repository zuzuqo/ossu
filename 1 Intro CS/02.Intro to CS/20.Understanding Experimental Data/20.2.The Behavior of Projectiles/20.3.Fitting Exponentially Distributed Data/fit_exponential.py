import math

import matplotlib
import numpy as np
from matplotlib import pyplot as plt


def create_data(f, x_vals):
    y_vals = []
    for i in x_vals:
        y_vals.append(f(i))
    return np.array(y_vals)


def fit_exp_data(x_vals, y_vals):
    log_vals = []
    for y in y_vals:
        log_vals.append(math.log(y, 2))
    fit = np.polyfit(x_vals, log_vals, 1)
    return fit, 2


if __name__ == '__main__':
    x_vals = range(10)
    f = lambda x: 3 ** x
    y_vals = create_data(f, x_vals)

    matplotlib.use('TkAgg')
    plt.plot(x_vals, y_vals, 'ko', label='Actual values')

    fit, base = fit_exp_data(x_vals, y_vals)
    predicted_y_vals = []
    for x in x_vals:
        predicted_y_vals.append(base ** np.polyval(fit, x))
    plt.plot(x_vals, predicted_y_vals, label='Predicted values')

    plt.title('Fitting an Exponential Function')
    plt.legend(loc='upper left')
    plt.savefig('fit-exp')
    plt.show()

    print(f'f(20) = {f(20)}')
    print(f'Predicted value = {int(base ** (np.polyval(fit, [20])))}')
