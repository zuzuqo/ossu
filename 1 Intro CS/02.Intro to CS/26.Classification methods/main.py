import random

import matplotlib
import numpy as np
import sklearn.linear_model as sklm
import sklearn.metrics as skm
from matplotlib import pyplot as plt

from evaluating_classifiers import get_stats, specificity, sensitivity
from k_nearest_neighbors import k_nearest_classify, prevalence_classify, find_k, regression_based_classifier
from predicting_gender import divide_80_20, build_marathon_examples


def multi_class_log_regression():
    feature_vecs, labels = [], []
    for i in range(25000):
        feature_vecs.append([random.gauss(0, .5), random.gauss(0, .5), random.random()])
        labels.append('A')
        feature_vecs.append([random.gauss(0, .5), random.gauss(2, 0), random.random()])
        labels.append('B')
        feature_vecs.append([random.gauss(2, .5), random.gauss(0, .5), random.random()])
        labels.append('C')
        feature_vecs.append([random.gauss(2, .5), random.gauss(2, 0), random.random()])
        labels.append('D')
    model = sklm.LogisticRegression().fit(feature_vecs, labels)
    print(f'model.classes_ = {model.classes_}')
    for i in range(len(model.coef_)):
        print(f'For label {model.classes_[i]}, feature weights = {model.coef_[i].round(4)}')
    print(f'[0, 0] probs = {model.predict_proba([[0, 0, 1]])[0].round(4)}')
    print(f'[0, 2] probs = {model.predict_proba([[0, 2, 2]])[0].round(4)}')
    print(f'[2, 0] probs = {model.predict_proba([[2, 0, 3]])[0].round(4)}')
    print(f'[2, 2] probs = {model.predict_proba([[2, 2, 4]])[0].round(4)}')


def two_class_log_regression():
    feature_vecs, labels = [], []
    for i in range(25000):
        feature_vecs.append([random.gauss(0, .5), random.gauss(0, .5), random.random()])
        labels.append('A')
        feature_vecs.append([random.gauss(0, .5), random.gauss(2, 0), random.random()])
        labels.append('B')
    model = sklm.LogisticRegression().fit(feature_vecs, labels)
    print(f'model.coef = {model.coef_.round(4)}')
    print(f'[0, 0] probs = {model.predict_proba([[0, 0, 1]])[0].round(4)}')
    print(f'[0, 2] probs = {model.predict_proba([[0, 2, 2]])[0].round(4)}')
    print(f'[2, 0] probs = {model.predict_proba([[2, 0, 3]])[0].round(4)}')
    print(f'[2, 2] probs = {model.predict_proba([[2, 2, 4]])[0].round(4)}')


def apply_model(model, test_set, label, prob=.5):
    test_feature_vecs = [e.get_features() for e in test_set]
    probs = model.predict_proba(test_feature_vecs)
    true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
    for i in range(len(probs)):
        if probs[i][1] > prob:
            if test_set[i].get_label() == label:
                true_pos += 1
            else:
                false_pos += 1
        else:
            if test_set[i].get_label() != label:
                true_neg += 1
            else:
                false_neg += 1
    return true_pos, false_pos, true_neg, false_neg


def build_ROC(model, test_set, label, title, plot=True):
    x_vals, y_vals = [], []
    for p in np.arange(0, 1, 0.01):
        true_pos, false_pos, true_neg, false_neg = apply_model(model, test_set, label, p)
        x_vals.append(1 - specificity(true_neg, false_pos))
        y_vals.append(sensitivity(true_pos, false_neg))
    auroc = skm.auc(x_vals, y_vals)
    if plot:
        matplotlib.use('TkAgg')
        plt.plot(x_vals, y_vals)
        plt.plot([0, 1], [0, 1, ], '--')
        plt.title(f'{title} (AUROC = {round(auroc, 3)})')
        plt.xlabel('1 - Specificity')
        plt.ylabel('Sensitivity')
        plt.savefig('auroc')
        plt.show()
    return auroc


if __name__ == '__main__':
    examples = build_marathon_examples('bm_results2012.csv')
    # training_set, test_set = divide_80_20(examples[:1000])
    training_set, test_set = divide_80_20(examples)

    # 26.3.K-nearest Neighbors

    # true_pos, false_pos, true_neg, false_neg = k_nearest_classify(training_set, test_set, 'M', 9)
    # true_pos, false_pos, true_neg, false_neg = prevalence_classify(training_set, test_set, 'M')
    # get_stats(true_pos, false_pos, true_neg, false_neg)
    # find_k(training_set, 1, 21, 5, 'M')

    # 26.4.Regression-based Classifiers
    # regression_based_classifier(training_set, test_set)

    # multi_class_log_regression()
    # two_class_log_regression()

    # use logistic regression to predict model
    feature_vecs, labels = [], []
    for e in training_set:
        feature_vecs.append([e.get_age(), e.get_time()])
        labels.append(e.get_label())
    model = sklm.LogisticRegression().fit(feature_vecs, labels)
    # print(f'Feature weights for label M:\n'
    #       f'age = {round(model.coef_[0][0], 3)},'
    #       f'time = {round(model.coef_[0][1], 3)}')
    # true_pos, false_pos, true_neg, false_neg = apply_model(model, test_set, 'M', .5)
    # get_stats(true_pos, false_pos, true_neg, false_neg)

    build_ROC(model, test_set, 'M', 'ROC for Predicting Gender')
