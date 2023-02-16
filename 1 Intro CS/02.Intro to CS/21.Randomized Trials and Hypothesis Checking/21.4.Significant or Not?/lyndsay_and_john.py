import random

import scipy


def game_sim():
    num_games = 1273
    lyndsay_wins = 666
    num_trials = 10000
    at_least = 0
    for t in range(num_trials):
        l_wins, j_wins = 0, 0
        for g in range(num_games):
            if random.random() < 0.5:
                l_wins += 1
            else:
                j_wins += 1
        if l_wins >= lyndsay_wins or j_wins >= lyndsay_wins:
            at_least += 1
    print(f'Probability of result at least this extreme by accident = {at_least / num_trials}')


if __name__ == '__main__':
    # num_games = 1273
    # lyndsay_wins = 666
    # outcomes = [1.0] * lyndsay_wins + [0] * (num_games - lyndsay_wins)
    # print(f'The p-value from a one-sample test is {scipy.stats.ttest_1samp(outcomes, 0.5)[1]}')

    game_sim()
