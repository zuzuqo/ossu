# geometric distribution example
import random

import matplotlib
from matplotlib import pyplot as plt


def successful_starts(success_prob, num_trials):
    tries_before_success = []
    for t in range(num_trials):
        consec_failures = 0
        while random.random() > success_prob:
            consec_failures += 1
            tries_before_success.append(consec_failures)
    return tries_before_success


if __name__ == '__main__':
    prob_of_success = .5
    num_trials = 5000
    distribution = successful_starts(prob_of_success, num_trials)

    matplotlib.use('TkAgg')
    plt.hist(distribution, bins=14)
    plt.xlabel('Tries Before Success')
    plt.ylabel(f'Number of Occurrences Out of {num_trials}')
    plt.title(f'Probability of Starting Each Try = {prob_of_success}')
    plt.savefig('successful_starts')
    plt.show()
