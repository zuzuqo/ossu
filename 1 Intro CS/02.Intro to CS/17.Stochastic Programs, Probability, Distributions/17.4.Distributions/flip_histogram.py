import random

import matplotlib
from matplotlib import pyplot as plt

from variance import standard_deviation


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


def label_plot(num_flips, num_trials, mean, sd):
    plt.title(f'{num_trials} trials of {num_flips} flips each')
    plt.xlabel('Fraction of Heads')
    plt.ylabel('Number of Trials')
    plt.annotate(f'Mean = {round(mean, 4)}\n'
                 f'SD = {round(sd, 4)}', size='x-large', xycoords='axes fraction', xy=(.67, .5))


def make_plots(num_flips1, num_flips2, num_trials):
    matplotlib.use('TkAgg')
    val1, mean1, sd1 = flip_sim(num_flips1, num_trials)
    plt.hist(val1, bins=20)
    x_min, x_max = plt.xlim()
    label_plot(num_flips1, num_trials, mean1, sd1)
    plt.savefig('plot-1')
    plt.show()
    plt.figure()
    val2, mean2, sd2 = flip_sim(num_flips2, num_trials)
    plt.hist(val2, bins=20)
    plt.xlim(x_min, x_max)
    label_plot(num_flips2, num_trials, mean2, sd2)
    plt.savefig('plot-2')
    plt.show()


if __name__ == '__main__':
    make_plots(100, 1000, 100000)
