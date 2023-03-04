import numpy as np
import pandas as pd
from example import Example
from kmeans import try_k_means
from scaling import z_scale, linear_scale


def read_data(filename, scale_method=None):
    df = pd.read_csv(filename, comment='#')
    df = df.set_index('Name')
    if scale_method is not None:
        for c in df.columns:
            df[c] = scale_method(df[c])
    feature_vector_list = [np.array(df.loc[i].values) for i in df.index]
    species_names = list(df.index)
    return {species_names[i]: feature_vector_list[i] for i in range(len(species_names))}


def build_mammal_examples(species_dict):
    examples = []
    for i in species_dict:
        example = Example(i, species_dict[i])
        examples.append(example)
    return examples


def test_teeth(filename, num_clusters, num_trials, scale_method=None):
    def print_clustering(clustering):
        for c in clustering:
            names = ''
            for p in c.members():
                names += f'{p.get_name()}, '
            print()
            print(names[:-2])

    species_dict = read_data(filename, scale_method)
    examples = build_mammal_examples(species_dict)
    print_clustering(try_k_means(examples, num_clusters, num_trials))


def add_labels(examples, label_file):
    df = pd.read_csv(label_file, comment='#')
    df = df.set_index('Name')
    for e in examples:
        if e.get_name() in df.index:
            e.set_label(df.loc[e.get_name()]['Diet'])


def check_diet(cluster):
    herbivores, carnivores, omnivores = 0, 0, 0
    for m in cluster.members():
        if m.get_label() == 0:
            herbivores += 1
        elif m.get_label() == 1:
            carnivores += 1
        else:
            omnivores += 1
    print(f'\t{herbivores} herbivores, {carnivores} carnivores, {omnivores} omnivores\n')


def test_teeth_diet(features_file, labels_file, num_clusters, num_trials, scale_method=None):
    def print_clustering(clustering):
        for c in clustering:
            names = ''
            for p in c.members():
                names += f'{p.get_name()}, '
            print()
            print(names[:-2])
            check_diet(c)
    species_dict = read_data(features_file, scale_method)
    examples = build_mammal_examples(species_dict)
    add_labels(examples, labels_file)
    print_clustering(try_k_means(examples, num_clusters, num_trials))


if __name__ == '__main__':
    # test_teeth('dentalFormulas.csv', 3, 40)
    # test_teeth('dentalFormulas.csv', 3, 40, z_scale)
    # test_teeth('dentalFormulas.csv', 3, 40, linear_scale)
    # test_teeth_diet('dentalFormulas.csv', 'diet.csv', 3, 40, z_scale)
    test_teeth_diet('dentalFormulas.csv', 'diet.csv', 3, 40, linear_scale)
