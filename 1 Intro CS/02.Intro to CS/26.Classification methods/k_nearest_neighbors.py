import random

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

from predicting_gender import divide_80_20
from evaluating_classifiers import accuracy, get_stats


def find_k_nearest(example, example_set, k):
    k_nearest, distances = [], []
    for i in range(k):
        k_nearest.append(example_set[i])
        distances.append(example.feature_dist(example_set[i]))
    max_dist = max(distances)
    for e in example_set[k:]:
        dist = example.feature_dist(e)
        if dist < max_dist:
            max_index = distances.index(max_dist)
            k_nearest[max_index] = e
            distances[max_index] = dist
            max_dist = max(distances)
    return k_nearest, distances


def k_nearest_classify(training_set, test_set, label, k):
    true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
    for e in test_set:
        # print(f'Classifying {e}')
        nearest, distances = find_k_nearest(e, training_set, k)
        num_match = 0
        for i in range(len(nearest)):
            if nearest[i].get_label() == label:
                num_match += 1
        if num_match > k // 2:
            if e.get_label() == label:
                true_pos += 1
            else:
                false_pos += 1
        else:
            if e.get_label() != label:
                true_neg += 1
            else:
                false_neg += 1
    return true_pos, false_pos, true_neg, false_neg


def prevalence_classify(training_set, test_set, label):
    num_with_label = 0
    for e in training_set:
        if e.get_label() == label:
            num_with_label += 1
    prob_label = num_with_label / len(training_set)
    true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
    for e in test_set:
        if random.random() < prob_label:
            if e.get_label() == label:
                true_pos += 1
            else:
                false_pos += 1
        else:
            if e.get_label() != label:
                true_neg += 1
            else:
                false_neg += 1
    return true_pos, false_pos, true_neg, false_neg


def find_k(training_set, min_k, max_k, num_folds, label):
    accuracies = []
    for k in range(min_k, max_k + 1, 2):
        score = 0
        for i in range(num_folds):
            fold = random.sample(training_set, min(5000, len(training_set)))
            examples, test_set = divide_80_20(fold)
            true_pos, false_pos, true_neg, false_neg = k_nearest_classify(examples, test_set, label, k)
            score += accuracy(true_pos, false_pos, true_neg, false_neg)
        accuracies.append(score / num_folds)
    matplotlib.use('TkAgg')
    plt.plot(range(min_k, max_k + 1, 2), accuracies)
    plt.title(f'Average Accuracy vs k ({num_folds} folds)')
    plt.xlabel('k')
    plt.ylabel('Accuracy')
    plt.savefig('find-k')
    plt.show()


def regression_based_classifier(training_set, test_set):
    age_m, age_w, time_m, time_w = [], [], [], []
    for e in training_set:
        if e.get_label() == 'M':
            age_m.append(e.get_age())
            time_m.append(e.get_time())
        else:
            age_w.append(e.get_age())
            time_w.append(e.get_time())
    ages, times = [], []
    for i in random.sample(range(len(age_m)), 300):
        ages.append(age_m[i])
        times.append(time_m[i])
    matplotlib.use('TkAgg')
    plt.plot(ages, times, 'yo', markersize=6, label='Men')
    ages, times = [], []
    for i in random.sample(range(len(age_w)), 300):
        ages.append(age_w[i])
        times.append(time_w[i])
    plt.plot(ages, times, 'k^', markersize=6, label='Women')
    m_model = np.polyfit(age_m, time_m, 1)
    f_model = np.polyfit(age_w, time_w, 1)
    x_min, x_max = 15, 85
    plt.plot((x_min, x_max), (np.polyval(m_model, (x_min, x_max))), 'k', label='Men')
    plt.plot((x_min, x_max), (np.polyval(f_model, (x_min, x_max))), 'k--', label='Women')
    plt.title('Linear Regression Models')
    plt.xlabel('Age')
    plt.ylabel('Finishing time (minutes)')
    plt.legend(loc='best')
    plt.savefig('regression-classifier')
    plt.show()

    true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
    for e in test_set:
        age = e.get_age()
        time = e.get_time()
        if abs(time - np.polyval(m_model, age)) < abs(time - np.polyval(f_model, age)):
            if e.get_label() == 'M':
                true_pos += 1
            else:
                false_pos += 1
        else:
            if e.get_label() == 'F':
                true_neg += 1
            else:
                false_neg += 1
    get_stats(true_pos, false_pos, true_neg, false_neg)
