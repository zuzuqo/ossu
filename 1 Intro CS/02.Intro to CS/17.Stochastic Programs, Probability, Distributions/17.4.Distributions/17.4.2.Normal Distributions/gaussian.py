import random

import numpy as np
from scipy.integrate import quad


def gaussian(x, mu, sigma):
    factor1 = 1 / (sigma * ((2 * np.pi) ** .5))
    factor2 = np.e ** -(((x - mu) ** 2) / (2 * sigma ** 2))
    return factor1 * factor2


def check_empirical(mu_max, sigma_max, num_trials):
    for t in range(num_trials):
        mu = random.randint(-mu_max, mu_max + 1)
        sigma = random.randint(1, sigma_max)
        print(f'For mu = {mu} and sigma = {sigma}')
        for num_std in range(1, 4):
            area = quad(gaussian, mu - num_std * sigma, mu + num_std * sigma, (mu, sigma))[0]
            print(f'\tFraction within {num_std} std = {round(area, 4)}')


if __name__ == '__main__':
    check_empirical(10, 10, 3)
