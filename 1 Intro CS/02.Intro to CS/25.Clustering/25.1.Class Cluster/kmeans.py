import random

import matplotlib
import matplotlib.pyplot as plt
from cluster import Cluster
from example import Example


def k_means(examples, k, verbose=False):
    initial_centroids = random.sample(examples, k)
    clusters = []
    for e in initial_centroids:
        clusters.append(Cluster([e]))

    converged = False
    num_iterations = 0
    while not converged:
        num_iterations += 1
        new_clusters = []
        for i in range(k):
            new_clusters.append([])

        for e in examples:
            smallest_distance = e.distance(clusters[0].get_centroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].get_centroid())
                if distance < smallest_distance:
                    smallest_distance = distance
                    index = i
            new_clusters[index].append(e)
        for c in new_clusters:
            if len(c) == 0:
                raise ValueError('Empty Cluster')

        converged = True
        for i in range(k):
            if clusters[i].update(new_clusters[i]) > 0:
                converged = False
        if verbose:
            print(f'Iteration #{num_iterations}')
            for c in clusters:
                print(c)
            print()
        return clusters


def dissimilarity(clusters):
    tot_dist = 0
    for c in clusters:
        tot_dist += c.variability()
    return tot_dist


def try_k_means(examples, num_clusters, num_trials, verbose=False):
    best = k_means(examples, num_clusters, verbose)
    min_dissimilarity = dissimilarity(best)
    trial = 1
    while trial < num_trials:
        try:
            clusters = k_means(examples, num_clusters, verbose)
        except ValueError:
            continue
        curr_dissimilarity = dissimilarity(clusters)
        if curr_dissimilarity < min_dissimilarity:
            best = clusters
            min_dissimilarity = curr_dissimilarity
        trial += 1
    return best


def gen_distribution(x_mean, x_sd, y_mean, y_sd, n, name_prefix):
    samples = []
    for s in range(n):
        x = random.gauss(x_mean, x_sd)
        y = random.gauss(y_mean, y_sd)
        samples.append(Example(name_prefix + str(s), [x, y]))
    return samples


def plot_samples(samples, marker):
    x_vals, y_vals = [], []
    for s in samples:
        x, y = s.get_features()[0], s.get_features()[1]
        plt.annotate(s.get_name(), xy=(x, y), xytext=(x + 0.13, y - 0.07), fontsize='x-large')
        x_vals.append(x)
        y_vals.append(y)
    plt.plot(x_vals, y_vals, marker)


def contrived_test(num_trials, k, verbose=False):
    x_mean = 3
    x_sd = 1
    y_mean = 5
    y_sd = 1
    n = 10
    matplotlib.use('TkAgg')
    d1_samples = gen_distribution(x_mean, x_sd, y_mean, y_sd, n, 'A')
    plot_samples(d1_samples, 'k^')
    d2_samples = gen_distribution(x_mean + 3, x_sd, y_mean + 1, y_sd, n, 'B')
    plot_samples(d2_samples, 'ko')
    plt.show()
    clusters = try_k_means(d1_samples + d2_samples, k, num_trials, verbose)
    print('Final result')
    for c in clusters:
        print(c)


def contrived_test_2(num_trials, k, verbose=False):
    x_mean = 3
    x_sd = 1
    y_mean = 5
    y_sd = 1
    n = 8
    matplotlib.use('TkAgg')
    d1_samples = gen_distribution(x_mean, x_sd, y_mean, y_sd, n, 'A')
    plot_samples(d1_samples, 'k^')
    d2_samples = gen_distribution(x_mean + 3, x_sd, y_mean, y_sd, n, 'B')
    plot_samples(d2_samples, 'ko')
    d3_samples = gen_distribution(x_mean, x_sd, y_mean + 3, y_sd, n, 'C')
    plot_samples(d3_samples, 'kx')
    clusters = try_k_means(d1_samples + d2_samples + d3_samples, k, num_trials, verbose)
    plt.ylim(0, 12)
    plt.show()
    print(f'Final result has dissimilarity {round(dissimilarity(clusters), 3)}')
    for c in clusters:
        print(c)


if __name__ == '__main__':
    contrived_test_2(40, 3)
