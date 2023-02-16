import random

import scipy.stats


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


def compare_mean_marathon_data_by_country(data):
    countries_to_compare = ['BEL', 'BRA', 'FRA', 'JPN', 'ITA']

    country_times = {}
    for i in range(len(data['name'])):
        if data['country'][i] in countries_to_compare and data['gender'][i] == 'F':
            try:
                country_times[data['country'][i]].append(data['time'][i])
            except KeyError:
                country_times[data['country'][i]] = [data['time'][i]]

    for c1 in countries_to_compare:
        for c2 in countries_to_compare:
            if c1 < c2:
                p_val = scipy.stats.ttest_ind(country_times[c1], country_times[c2], equal_var=False)[1]
                if p_val < 0.05:
                    print(f'{c1} and {c2} have significantly different means\n'
                          f'p-value = {round(p_val, 4)}')


def check_multiply_hypotheses(num_hyps=50, sample_size=200):
    population = []
    for i in range(5000):
        population.append(random.gauss(0, 1))
    sample_1s, sample_2s = [], []

    # gen many pairs of small samples
    for i in range(num_hyps):
        sample_1s.append(random.sample(population, sample_size))
        sample_2s.append(random.sample(population, sample_size))
    # check pairs for statistically significant difference
    num_sig = 0
    for i in range(num_hyps):
        if scipy.stats.ttest_ind(sample_1s[i], sample_2s[i])[1] < 0.05:
            num_sig += 1
    print(f'# of statically significantly different (p < 0.05) pairs = {num_sig}')


if __name__ == '__main__':
    data = get_bm_data('bm_results2012.csv')
    compare_mean_marathon_data_by_country(data)
    check_multiply_hypotheses()