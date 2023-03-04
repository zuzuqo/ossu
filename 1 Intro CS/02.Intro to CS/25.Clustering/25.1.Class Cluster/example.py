def minkowski_dist(v1, v2, p):
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i]) ** p
    return dist ** (1 / p)


class Example(object):

    def __init__(self, name, features, label=None):
        self.name = name
        self.features = features
        self.label = label

    def dimensionality(self):
        return len(self.features)

    def set_label(self, label):
        self.label = label

    def get_features(self):
        return self.features[:]

    def get_label(self):
        return self.label

    def get_name(self):
        return self.name

    def distance(self, other):
        return minkowski_dist(self.features, other.get_features(), 2)

    def __str__(self):
        return '{}:{}:{}'.format(self.name, self.features, self.label)
