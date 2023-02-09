import random

import matplotlib
from matplotlib import pyplot as plt
from variance import standard_deviation, coefficient_variation


def flip(num_flip: int, choice=('H', 'T'), goal='H'):
    heads = 0
    for i in range(num_flip):
        if random.choice(choice) == goal:
            heads += 1
    return heads / num_flip


def flip_simulation(num_flips_per_trial, num_trials, func=flip):
    frac_heads = []
    for i in range(num_trials):
        frac_heads.append(func(num_flips_per_trial))
    mean = sum(frac_heads) / len(frac_heads)
    return mean


def regress_to_mean(num_flips, num_trials):
    frac_heads = []
    for t in range(num_trials):
        frac_heads.append(flip(num_flips))
    extremes, next_trials = [], []
    for i in range(len(frac_heads) - 1):
        if frac_heads[i] < .34 or frac_heads[i] > .66:
            extremes.append(frac_heads[i])
            next_trials.append(frac_heads[i + 1])

    matplotlib.use('TkAgg')
    plt.plot(range(len(extremes)), extremes, 'ko', label='Extreme')
    plt.plot(range(len(next_trials)), next_trials, 'k^', label='Next Trial')
    plt.axhline(0.5)
    plt.ylim(0, 1)
    plt.xlim(-1, len(extremes) + 1)
    plt.xlabel('Extreme Example and Next Trial')
    plt.ylabel('Fraction Heads')
    plt.title('Regression to the Mean')
    plt.legend(loc='best')
    plt.savefig('regress-to-mean')
    plt.show()


def flip_plot_old(min_exp, max_exp):
    ratios, diffs, x_axis = [], [], []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2 ** exp)
    for num_flips in x_axis:
        num_heads = 0
        for n in range(num_flips):
            if random.choice(('H', 'T')) == 'H':
                num_heads += 1
        num_tails = num_flips - num_heads
        try:
            ratios.append(num_heads / num_tails)
            diffs.append(abs(num_heads - num_tails))
        except ZeroDivisionError:
            continue

    matplotlib.use('TkAgg')
    plt.title('Difference Between Heads and Tails')
    plt.xlabel('Number of Flips')
    plt.ylabel('Abs(#Heads - #Tails)')
    plt.xticks(rotation='vertical')
    plt.plot(x_axis, diffs, 'ko')
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('flip-plot-difference')
    plt.figure()
    plt.title('Heads/Tails Ratios')
    plt.xlabel('Number of Flips')
    plt.ylabel('#Heads / #Tails')
    plt.xticks(rotation='vertical')
    plt.plot(x_axis, ratios, 'ko')
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('flip-plot-ratio')
    plt.show()


def make_plot(x_vals, y_vals, title, x_label, y_label, style, log_x=False, log_y=False, save=''):
    matplotlib.use('TkAgg')
    plt.figure()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x_vals, y_vals, style)
    if log_x:
        plt.semilogx()
    if log_y:
        plt.semilogy()
    if save != '':
        plt.savefig(save)
    plt.show()


def run_trial(num_flips):
    num_heads = 0
    for n in range(num_flips):
        if random.choice(('H', 'T')) == 'H':
            num_heads += 1
    num_tails = num_flips - num_heads
    return num_heads, num_tails


def flip_plot(min_exp, max_exp, num_trials):
    x_axis, ratios_means, diffs_means, ratios_sds, diffs_sds = [], [], [], [], []
    ratios_cv, diffs_cv = [], []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2 ** exp)
    for num_flips in x_axis:
        ratios, diffs = [], []
        for t in range(num_trials):
            num_heads, num_tails = run_trial(num_flips)
            ratios.append(num_heads / num_tails)
            diffs.append(abs(num_heads - num_tails))
        ratios_means.append(sum(ratios) / num_trials)
        diffs_means.append(sum(diffs) / num_trials)
        ratios_sds.append(standard_deviation(ratios))
        diffs_sds.append(standard_deviation(diffs))
        ratios_cv.append(coefficient_variation(ratios))
        diffs_cv.append(coefficient_variation(diffs))
    # mean
    title = f'Mean Heads/Tails Ratios ({num_trials} Trials)'
    make_plot(x_axis, ratios_means, title, 'Number of Flips', 'Mean Heads/Tails', 'ko', log_x=True,
              save='mean-ht-ratios')
    title = f'Mean Heads/Tails Ratios ({num_trials} Trials)'
    make_plot(x_axis, diffs_means, title, 'Number of Flips', 'Mean Heads/Tails', 'ko', log_x=True,
              save='mean-ht-diffs')
    # standard deviation
    title = f'SD Heads/Tails Ratios ({num_trials} Trials)'
    make_plot(x_axis, ratios_sds, title, 'Number of Flips', 'Standard Deviation', 'ko', log_x=True, log_y=True,
              save='sd-ht-ratios')
    title = f'SD Heads/Tails Ratios ({num_trials} Trials)'
    make_plot(x_axis, diffs_sds, title, 'Number of Flips', 'Standard Deviation', 'ko', log_x=True, log_y=True,
              save='sd-ht-diffs')
    # coefficient of variation
    title = f'Coeff. of Variation Heads/Tails Ratios ({num_trials} Trials)'
    make_plot(x_axis, ratios_cv, title, 'Number of Flips', 'Mean Heads/Tails', 'ko', log_x=True,
              save='cv-ht-ratios')
    title = f'Coeff. of Variation Heads/Tails Ratios ({num_trials} Trials)'
    make_plot(x_axis, diffs_cv, title, 'Number of Flips', 'Standard Deviation', 'ko', log_x=True, log_y=True,
              save='cv-ht-diffs')

if __name__ == '__main__':
    # print(flip_simulation(10, 100))
    # regress_to_mean(15, 50)
    random.seed(0)
    # flip_plot_old(4, 20)
    flip_plot(4, 20, 20)
