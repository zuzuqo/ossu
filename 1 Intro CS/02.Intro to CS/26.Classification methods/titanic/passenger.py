import pandas as pd
from scipy.spatial import distance


class Passenger(object):
    features = ('1st Class', '2nd Class', '3rd Class', 'age', 'male')

    def __init__(self, p_class, age, gender, survived, name):
        self.name = name
        self.feature_vec = [0, 0, 0, age, gender]
        self.feature_vec[p_class - 1] = 1
        self.label = survived
        self.cabin_class = p_class

    def distance(self, other):
        # changed
        return distance.minkowski(self.feature_vec, other.feature_vec, 2)

    def get_class(self):
        return self.cabin_class

    def get_age(self):
        return self.feature_vec[3]

    def get_gender(self):
        return self.feature_vec[4]

    def get_name(self):
        return self.name

    def get_features(self):
        return self.feature_vec[:]

    def get_label(self):
        return self.label


def build_Titanic_examples():
    manifest = pd.read_csv('titanic_passengers.csv')
    examples = []
    for index, row in manifest.iterrows():
        p = Passenger(row['Class'], row['Age'], 1 if row['Gender'] == 'M' else 0, row['Survived'],
                      row['Last Name'] + row['Other Names'])
        examples.append(p)
    return examples

