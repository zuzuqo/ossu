import matplotlib.pyplot as plt
import matplotlib


def ex1():
    matplotlib.use('TkAgg')
    plt.plot([1, 2, 3, 4], [1, 7, 3, 5])
    plt.show()


def ex2():
    matplotlib.use('TkAgg')
    plt.figure(1)
    plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
    plt.figure(2)
    plt.plot([1, 4, 2, 3], [5, 6, 7, 8])
    plt.savefig('Figure-Addie')
    plt.figure(1)
    plt.plot([5, 6, 10, 3])
    plt.savefig('Figure-Jane')
    plt.show()


def ex3():
    matplotlib.use('TkAgg')
    principal = 10000
    interest_rate = .05
    years = 20
    values = []
    for i in range(years + 1):
        values.append(principal)
        principal += principal * interest_rate

    plt.plot(values)
    plt.title('5% Growth, Compounded Annually')
    plt.xlabel('Years of Compounding')
    plt.ylabel('Value of Principal ($)')
    plt.show()


def ex4():
    matplotlib.use('TkAgg')
    principal = 10000
    interest_rate = .05
    years = 20
    values = []
    for i in range(years + 1):
        values.append(principal)
        principal += principal * interest_rate

    plt.plot(values, 'ko')
    plt.title('5% Growth, Compounded Annually')
    plt.xlabel('Years of Compounding')
    plt.ylabel('Value of Principal ($)')
    plt.show()


def ex5():
    matplotlib.use('TkAgg')
    principal = 10000
    interest_rate = .05
    years = 20
    values = []
    for i in range(years + 1):
        values.append(principal)
        principal += principal * interest_rate

    plt.plot(values, '-k', linewidth=30)
    plt.title('5% Growth, Compounded Annually', fontsize='xx-large')
    plt.xlabel('Years of Compounding', fontsize='x-small')
    plt.ylabel('Value of Principal ($)')
    plt.show()


def ex6():
    matplotlib.use('TkAgg')
    principal = 10000
    interest_rate = .05
    years = 20
    values = []
    for i in range(years + 1):
        values.append(principal)
        principal += principal * interest_rate

    plt.rcParams['lines.linewidth'] = 6
    plt.plot(values)
    plt.title('5% Growth, Compounded Annually')
    plt.xlabel('Years of Compounding')
    plt.ylabel('Value of Principal ($)')
    plt.show()


def ex7():
    matplotlib.use('TkAgg')
    principal = 10000
    interest_rate = .05
    years = 20
    values = []
    for i in range(years + 1):
        values.append(principal)
        principal += principal * interest_rate

    # set line width
    plt.rcParams['lines.linewidth'] = 6
    # set font size for titles
    plt.rcParams['axes.titlesize'] = 20
    # set font size for labels on axes
    plt.rcParams['axes.labelsize'] = 20
    # set size of numbers on x-axis
    plt.rcParams['xtick.labelsize'] = 16
    # set size of numbers on y-axis
    plt.rcParams['ytick.labelsize'] = 16
    # set size of ticks on x-axis
    plt.rcParams['xtick.major.size'] = 7
    # set size of ticks on y-axis
    plt.rcParams['ytick.major.size'] = 7
    # set size of markers, e.g., circles representing points
    plt.rcParams['lines.markersize'] = 10
    # set number of times marker is shown when displaying legend
    plt.rcParams['legend.numpoints'] = 1
    # Set size of type in legend
    plt.rcParams['legend.fontsize'] = 14

    plt.plot(values)
    plt.title('5% Growth, Compounded Annually')
    plt.xlabel('Years of Compounding')
    plt.ylabel('Value of Principal ($)')
    plt.show()

ex7()
