import random
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

def variance(x: list):
    mean = sum(x) / len(x)
    tot = 0
    for i in x:
        tot += (i - mean) ** 2
    return tot / len(x)


def standard_deviation(x: list):
    return variance(x) ** .5

def flip(num_flips):
    heads = 0
    for i in range(num_flips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads / num_flips


def flip_sim(num_flips_per_trial, num_trials):
    frac_heads = []
    for i in range(num_trials):
        frac_heads.append(flip(num_flips_per_trial))
    mean = sum(frac_heads) / len(frac_heads)
    sd = standard_deviation(frac_heads)
    return frac_heads, mean, sd


def show_error_bars(min_exp, max_exp, num_trials):
    means, sds, x_vals = [], [], []
    for exp in range(min_exp, max_exp + 1):
        x_vals.append(2 ** exp)
        frac_heads, mean, sd = flip_sim(2 ** exp, num_trials)
        means.append(mean)
        sds.append(sd)
    matplotlib.use('TkAgg')
    plt.errorbar(x_vals, means, yerr=1.96 * np.array(sds))
    plt.semilogx()
    plt.title(f'Mean Fraction of Heads ({num_trials} trials)')
    plt.xlabel('Number of flips per trial')
    plt.ylabel('Fraction of heads & 95% confidence')
    plt.savefig('error-bars')
    plt.show()


if __name__ == '__main__':
    show_error_bars(3, 10, 100)
