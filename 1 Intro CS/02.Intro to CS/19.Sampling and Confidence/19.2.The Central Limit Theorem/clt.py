import random

import matplotlib
import numpy as np
from matplotlib import pyplot as plt


def plot_means(num_dice_per_trial, num_dice_thrown, num_bins, legend, color, style, save=False):
    means = []
    num_trials = num_dice_thrown // num_dice_per_trial
    for i in range(num_trials):
        vals = 0
        for j in range(num_dice_per_trial):
            vals += 5 * random.random()
        means.append(vals / num_dice_per_trial)

    matplotlib.use('TkAgg')
    plt.hist(means, num_bins, color=color, label=legend, weights=np.array(len(means) * [1]) / len(means), hatch=style)
    plt.title('Rolling Continuous Dice')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.legend(loc='upper left')
    if save:
        plt.savefig(f'rolling-dice-{num_dice_per_trial}')
        plt.show()
    return sum(means) / len(means), np.var(means)


if __name__ == '__main__':
    mean, var = plot_means(1, 10000, 11, '1 die', 'y', '*')
    print(f'Mean of rolling 1 die = {round(mean, 4)}\n'
          f'Variance = {round(var, 4)}')
    mean, var = plot_means(100, 10000, 11, 'Mean 100 dice', 'c', '//')
    print(f'Mean of rolling 100 dice = {round(mean, 4)}\n'
          f'Variance = {round(var, 4)}')
    plt.savefig('rolling-dice-1-100')
    plt.show()
