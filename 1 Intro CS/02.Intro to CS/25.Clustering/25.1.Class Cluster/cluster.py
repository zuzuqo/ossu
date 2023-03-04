import numpy as np
from example import Example


class Cluster(object):

    def __init__(self, examples):
        self.examples = examples
        self.centroid = self.compute_centroid()

    def update(self, examples):

        old_centroid = self.centroid
        self.examples = examples
        self.centroid = self.compute_centroid()
        return old_centroid.distance(self.centroid)

    def compute_centroid(self):
        vals = np.array([0.0] * self.examples[0].dimensionality())
        for e in self.examples:
            vals += e.get_features()
        centroid = Example('centroid', vals / len(self.examples))
        return centroid

    def get_centroid(self):
        return self.centroid

    def variability(self):
        tot_dist = 0.0
        for e in self.examples:
            tot_dist += (e.distance(self.centroid)) ** 2
        return tot_dist

    def members(self):
        for e in self.examples:
            yield e

    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.get_name())
        names.sort()
        result = ('Cluster with centroid '
                  + str(self.centroid.get_features()) + ' contains:\n  ')
        for e in names:
            result = result + e + ', '
        return result[:-2]


if __name__ == '__main__':
    rattlesnake = Example('rattlesnake', [1, 1, 1, 1, 0])
    boa = Example('boa', [0, 1, 0, 1, 0])
    dart_frog = Example('dart frog', [1, 0, 1, 0, 4])
    alligator = Example('alligator', [1, 1, 0, 1, 4])
    my_examples = [rattlesnake, boa, dart_frog, alligator]
    c = Cluster(my_examples)
    print(c)
