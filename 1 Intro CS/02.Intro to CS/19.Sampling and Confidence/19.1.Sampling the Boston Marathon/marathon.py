import random

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def get_bm_data(filename):
    data = {}
    with open(filename, 'r') as f:
        f.readline()
        line = f.readline()
        for k in ('name', 'gender', 'age', 'division', 'country', 'time'):
            data[k] = []
        while line != '':
            split = line.split(',')
            data['name'].append(split[0])
            data['gender'].append(split[1])
            data['age'].append(split[2])
            data['division'].append(split[3])
            data['country'].append(split[4])
            data['time'].append(float(split[5][:-1]))
            line = f.readline()
    return data


def make_hist(data, bins, title, x_label, y_label, hist_name):
    matplotlib.use('TkAgg')
    plt.hist(data, bins)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    mean = sum(data) / len(data)
    std = np.std(data)
    plt.annotate(f'Mean = {round(mean, 2)}\n'
                 f'SD = {round(std, 2)}\n',
                 fontsize=14, xy=(.65, .75), xycoords='axes fraction')
    plt.savefig(hist_name)
    plt.show()


def sample_times(times, num_examples):
    sample = random.sample(times, num_examples)
    make_hist(sample, 10, f'Sample of Size {num_examples}', 'Minutes to Complete Race', 'Number of Runners',
              f'marathon-sample-{num_examples}')


def gaussian(x, mu, sigma):
    factor1 = 1 / (sigma * ((2 * np.pi) ** .5))
    factor2 = np.e ** -(((x - mu) ** 2) / (2 * sigma ** 2))
    return factor1 * factor2


def test_samples(num_trials, sample_size):
    tight_means, wide_means = [], []
    for t in range(num_trials):
        sample_tight, sample_wide = [], []
        for i in range(sample_size):
            sample_tight.append(random.gauss(0, 1))
            sample_wide.append(random.gauss(0, 100))
        tight_means.append(sum(sample_tight) / len(sample_tight))
        wide_means.append(sum(sample_wide) / len(sample_wide))
    return tight_means, wide_means


if __name__ == '__main__':
    times = get_bm_data('bm_results2012.csv')['time']
    # make_hist(times, 20, '2012 Boston Marathon', 'Minutes to Complete Race', 'Number of Runners', 'marathon-full')
    # sample_times(times, 50)
    # sample_times(times, 300)
    # sample_times(times, 1000)
    # sample_times(times, 5000)
    # area = round(quad(gaussian, -3, 3, (0, 1))[0], 4)
    # print(f'Probability of being within 3 of true mean of tight dist. = {area}')
    # area = round(quad(gaussian, -3, 3, (0, 100))[0], 4)
    # print(f'Probability of being within 3 of true mean of wide dist. = {area}')

    # num_trials = 1000
    # sample_size = 40
    # tight_means, wide_means = test_samples(num_trials, sample_size)
    #
    # matplotlib.use('TkAgg')
    # plt.plot(wide_means, 'y*', label='SD = 100')
    # plt.plot(tight_means, 'bo', label='SD = 1')
    # plt.xlabel('Sample Number')
    # plt.ylabel('Sample Mean')
    # plt.title(f'Means of Samples of Size {num_trials}')
    # plt.legend()
    # plt.savefig(f'means-of-samples-{sample_size}')
    # plt.show()
    #
    # plt.figure()
    # plt.hist(wide_means, bins=20, label='SD = 100')
    # plt.title('Distribution of Sample Means')
    # plt.xlabel('Sample Mean')
    # plt.ylabel('Frequency of Occurrence')
    # plt.legend()
    # plt.savefig(f'distribution-of-sample-means-{sample_size}')
    # plt.show()

    # # 19.2.CLT - plot with error bar
    # mean_of_means, std_of_means = [], []
    # sample_sizes = range(100, 1501, 200)
    # for sample_size in sample_sizes:
    #     sample_means = []
    #     for t in range(200):
    #         sample = random.sample(times, sample_size)
    #         sample_means.append(sum(sample) / sample_size)
    #     mean_of_means.append(sum(sample_means) / len(sample_means))
    #     std_of_means.append(np.std(sample_means))
    #
    # matplotlib.use('TkAgg')
    # plt.errorbar(sample_sizes, mean_of_means, color='c', yerr=1.96 * np.array(std_of_means),
    #              label='Estimated mean and 95% CI')
    # plt.axhline(sum(times) / len(times), linestyle='--', color='k', label='Population mean')
    # plt.title('Estimates of Mean Finishing Time')
    # plt.xlabel('Sample Size')
    # plt.ylabel('Finishing Time (minutes)')
    # plt.legend(loc='best')
    # plt.savefig('est-mean-finishing-time')
    # plt.show()

    # # 19.3. SEM or SE
    # pos_std = np.std(times)
    # sample_sizes = range(2, 200 , 2)
    # diffs_means = []
    # for sample_size in sample_sizes:
    #     diffs = []
    #     for t in range(100):
    #         diffs.append(abs(pos_std - np.std(random.sample(times, sample_size))))
    #     diffs_means.append(sum(diffs)/len(diffs))
    #
    # matplotlib.use('TkAgg')
    # plt.plot(sample_sizes, diffs_means)
    # plt.xlabel('Sample Size')
    # plt.ylabel('Abs(Pop.Std. - Sample Std.)')
    # plt.title('Error in Sample SD vs. Sample Size')
    # plt.savefig('sample-sd')
    # plt.show()

    # example with 200 runners
    # using se (standard error of means) to check distribution
    pop_mean = sum(times) / len(times)
    sample_size = 200
    num_bad = 0
    length = 10000
    for t in range(length):
        sample = random.sample(times, sample_size)
        sample_mean = sum(sample) / sample_size
        se = np.std(sample) / sample_size ** .5
        if abs(pop_mean - sample_mean) > 1.96 * se:
            num_bad += 1
    print(f'Fraction outside 95% confidence interval = {num_bad / length}')
    # if result is about 5% means good distribution
    # 95% within +-1.96*se
