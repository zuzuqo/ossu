import random

import numpy as np


def throw_needles(num_needles):
    in_circle = 0
    for Needles in range(1, num_needles + 1):
        x = random.random()
        y = random.random()
        if (x * x + y * y) ** .5 <= 1:
            in_circle += 1
    # counting needles in one quadrant only, so multiply by 4
    return 4 * (in_circle / num_needles)


def get_est(num_needles, num_trials):
    estimates = []
    for t in range(num_trials):
        pi_guess = throw_needles(num_needles)
        estimates.append(pi_guess)
    std_dev = np.std(estimates)
    cur_est = sum(estimates) / len(estimates)
    print(f'Est. = {round(cur_est, 5)}\n'
          f'Std.Dev. = {std_dev}\n'
          f'Needles = {num_needles}')
    return cur_est, std_dev


def est_pi(precision, num_trials):
    num_needles = 1000
    std_dev = precision
    while std_dev > precision / 1.96:
        cur_est, std_dev = get_est(num_needles, num_trials)
        num_needles *= 2
    return cur_est


if __name__ == '__main__':
    est_pi(0.01, 100)
