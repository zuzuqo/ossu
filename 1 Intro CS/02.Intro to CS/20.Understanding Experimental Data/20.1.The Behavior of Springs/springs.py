import matplotlib
import numpy as np
from matplotlib import pyplot as plt


def get_data(input_file):
    with open(input_file, 'r') as file:
        distances = []
        masses = []
        file.readline()
        for line in file:
            d, m = line.split(',')
            distances.append(float(d))
            masses.append(float(m))
    return masses, distances


def plot_data(input_file):
    masses, distances = get_data(input_file)
    distances = np.array(distances)
    masses = np.array(masses)
    forces = masses * 9.81

    matplotlib.use('TkAgg')
    plt.plot(forces, distances, 'bo')
    plt.title('Measured Displacement of Spring')
    plt.xlabel('|Force| (Newtons)')
    plt.ylabel('Distance (meters)')
    plt.savefig('springs')
    plt.show()


def fit_data(input_file):
    masses, distances = get_data(input_file)
    distances = np.array(distances[:-6])
    masses = np.array(masses[:-6])
    forces = masses * 9.81

    matplotlib.use('TkAgg')
    plt.plot(forces, distances, 'ko', label='Measured displacements')
    plt.title('Measured Displacement of Spring')
    plt.xlabel('|Force| (Newtons)')
    plt.ylabel('Distance (meters)')

    # find linear fit
    a, b = np.polyfit(forces, distances, 1)
    predicted_distances = a * np.array(forces) + b
    k = 1 / a
    plt.plot(forces, predicted_distances, label=f'Linear fit, k={k:.4f}')

    fit = np.polyfit(forces, distances, 3)
    forces = np.append(forces, 1.5*9.81)
    predicted_distances = np.polyval(fit, forces)
    plt.plot(forces, predicted_distances, 'k:', label=f'cubic fit')

    plt.legend(loc='best')
    plt.savefig(f'springs-polyfit-[:-6]')
    plt.show()


if __name__ == '__main__':
    fit_data('spring_data.csv')
