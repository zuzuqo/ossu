import matplotlib
from matplotlib import pyplot as plt

from binomial_distribution import binomial_distribution


def die_simulation(num_trials, num_repeats, n=6):
    '''using binomial distribution'''
    res = []
    for num_throws in range(2, num_trials + 2):
        res.append(binomial_distribution(num_throws, num_repeats, 1 / n))
    return res


def plot_bd(bd_res):
    matplotlib.use('TkAgg')
    plt.title('Probably of rolling two 3\'s in N rolls a fair die.')
    plt.plot(bd_res)
    plt.xlabel('Num trials')
    plt.ylabel('Probably')
    plt.savefig('die-bd')
    plt.show()


plot_bd(die_simulation(100, 2))
