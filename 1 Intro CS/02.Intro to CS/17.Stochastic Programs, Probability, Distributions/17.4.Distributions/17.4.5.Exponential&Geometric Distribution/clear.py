import matplotlib
from matplotlib import pyplot as plt


# exponential distributing ex
def clear(n, p, steps):
    """Assumes n & steps positive ints, p a float
         n: the initial number of molecules
         p: the probability of a molecule being cleared
         steps: the length of the simulation"""
    num_remaining = [n]
    for t in range(steps):
        num_remaining.append(n * ((1 - p) ** t))

    matplotlib.use('TkAgg')
    plt.plot(num_remaining)
    plt.xlabel('Time')
    plt.ylabel('Molecules Remaining')
    plt.title('Clearance of Drug')
    plt.semilogy()
    plt.savefig('clear-log')
    plt.show()


if __name__ == '__main__':
    clear(1000, .01, 1000)
