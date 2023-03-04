import random

import matplotlib
import numpy as np
from matplotlib import pyplot as plt
import sklearn.linear_model as sklm
import sklearn.metrics as skm
from passenger import Passenger, build_Titanic_examples
from evaluating_classifiers import specificity, sensitivity, get_stats


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


def summarize_stats(stats):
    def print_stat(x, name):
        mean = round(sum(x) / len(x), 3)
        std = np.std(x)
        print(f'Mean {name} = {mean}, '
              f'95% conf. int. = {round(mean - 1.96 * std, 3)} '
              f'to {round(mean + 1.96 * std, 3)}')

    accs, sens, specs, ppvs, auroc = [], [], [], [], []
    for stat in stats:
        accs.append(stat[0])
        sens.append(stat[1])
        specs.append(stat[2])
        ppvs.append(stat[3])
        auroc.append(stat[4])
    print_stat(accs, 'accuracy')
    print_stat(sens, 'sensitivity')
    print_stat(specs, 'specificity')


def divide_80_20(examples):
    sample_indices = random.sample(range(len(examples)), len(examples) // 5)
    training_set, test_set = [], []
    for i in range(len(examples)):
        if i in sample_indices:
            test_set.append(examples[i])
        else:
            training_set.append(examples[i])
    return training_set, test_set


def test_models(examples, num_trials, print_stats, print_weights):
    stats, weights = [], [[], [], [], [], []]
    for i in range(num_trials):
        training_set, test_set = divide_80_20(examples)
        x_vals, y_vals = [], []
        for e in training_set:
            x_vals.append(e.get_features())
            y_vals.append(e.get_label())
        x_vals = np.array(x_vals)
        y_vals = np.array(y_vals)
        model = sklm.LogisticRegression().fit(x_vals, y_vals)
        for i in range(len(Passenger.features)):
            weights[i].append(model.coef_[0][i])
        true_pos, false_pos, true_neg, false_neg = apply_model(model, test_set, 1, .5)
        auroc = build_ROC(model, test_set, 1, None, False)
        tmp = get_stats(true_pos, false_pos, true_neg, false_neg, False)
        stats.append(tmp + (auroc,))
    print(f'Avg for {num_trials} trials')
    if print_weights:
        print('Weights:')
        for feature in range(len(weights)):
            feature_mean = round(sum(weights[feature]) / num_trials, 3)
            feature_std = np.std(weights[feature])
            print(
                f'Mean weight {Passenger.features[feature]} = {feature_mean}, '
                f'95% conf. int = {round(feature_mean - 1.96 * feature_std, 3)} '
                f'to {round(feature_mean + 1.96 * feature_std, 3)}')
    if print_stats:
        print('Stats:')
        summarize_stats(stats)


if __name__ == '__main__':
    # correlation
    # manifest = pd.read_csv('titanic_passengers.csv')
    # manifest['Gender'] = (manifest['Gender'].apply(lambda g: 1 if g == 'M' else 0))
    # print(manifest.corr().round(2))

    test_models(build_Titanic_examples(), 100, True, True)
