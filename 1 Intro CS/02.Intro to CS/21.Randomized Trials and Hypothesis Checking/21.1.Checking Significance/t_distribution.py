import random

import matplotlib
import numpy as np
import scipy.stats
from matplotlib import pyplot as plt


def gen_data():
    random.seed(148)
    treatment_dist = (119.5, 5.0)
    control_dist = (120, 4.0)
    sample_size = 100
    treatment_times, control_times = [], []
    for s in range(sample_size):
        treatment_times.append(random.gauss(treatment_dist[0], treatment_dist[1]))
        control_times.append(random.gauss(control_dist[0], control_dist[1]))
    return control_times, treatment_times


def t_stat_p_value(control_times, treatment_times):
    control_mean = round(sum(control_times) / len(control_times), 2)
    treatment_mean = round(sum(treatment_times) / len(treatment_times), 2)
    print(f'Treatment mean - control mean = {round(treatment_mean - control_mean, 2)} minutes')
    two_sample_test = scipy.stats.ttest_ind(treatment_times, control_times, equal_var=False)
    print(f'The t-statistic from two-sample test is {round(two_sample_test[0], 2)}')
    print(f'The p-value from two-sample test is {round(two_sample_test[1], 2)}')


if __name__ == '__main__':
    t_stat = -2.26
    t_dist = []
    num_bins = 1000
    for i in range(100000):
        t_dist.append(np.random.standard_t(198))

    matplotlib.use('TkAgg')
    plt.hist(t_dist, bins=num_bins, weights=np.array(len(t_dist) * [1]) / len(t_dist))
    plt.axvline(t_stat, color='w')
    plt.axvline(-t_stat, color='w')
    plt.title('T-distribution with 198 Degrees of Freedom')
    plt.xlabel('T-statistic')
    plt.ylabel('Probably')
    plt.show()

    control_times, treatment_times = gen_data()
    t_stat_p_value(control_times, treatment_times)
    