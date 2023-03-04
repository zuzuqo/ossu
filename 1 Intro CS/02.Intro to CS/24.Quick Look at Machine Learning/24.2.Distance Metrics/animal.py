import matplotlib
import numpy as np
from matplotlib import pyplot as plt


def minkowski_dist(v1, v2, p):
    dist = 0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i]) ** p
    return dist ** (1 / p)


class Animal(object):
    def __init__(self, name, features):
        self._name = name
        self._features = np.array(features)

    def get_name(self):
        return self._name

    def get_features(self):
        return self._features

    def distance(self, other):
        return minkowski_dist(self.get_features(), other.get_features(), 2)


def compare_animals(animals, precision):
    column_labels = [a.get_name() for a in animals]
    row_labels = column_labels[:]
    table_vals = []
    for a1 in animals:
        row = []
        for a2 in animals:
            distance = a1.distance(a2)
            row.append(str(round(distance, precision)))
        table_vals.append(row)
    matplotlib.use('TkAgg')
    table = plt.table(rowLabels=row_labels,
                      colLabels=column_labels,
                      cellText=table_vals,
                      cellLoc='center',
                      loc='center',
                      colWidths=[0.2] * len(animals))
    plt.axis('off')
    table.scale(1, 2.5)
    plt.savefig('animal-distances')
    plt.show()


if __name__ == '__main__':
    rattlesnake = Animal('rattlesnake', [1, 1, 1, 1, 0])
    boa = Animal('boa', [0, 1, 0, 1, 0])
    dart_frog = Animal('dart frog', [1, 0, 1, 0, 4])
    alligator = Animal('alligator', [1, 1, 0, 1, 4])
    animals = [rattlesnake, boa, dart_frog, alligator]
    compare_animals(animals, 3)
