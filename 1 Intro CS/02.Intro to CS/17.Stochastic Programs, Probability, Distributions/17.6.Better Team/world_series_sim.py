import random

import matplotlib
import matplotlib.pyplot as plt


def play_series(num_games, team_prob):
    num_won = 0
    for game in range(num_games):
        if random.random() <= team_prob:
            num_won += 1
    return num_won > num_games // 2


def fraction_won(team_prob, num_series, series_len):
    won = 0
    for series in range(num_series):
        if play_series(series_len, team_prob):
            won += 1
    return won / num_series


def sim_series(num_series):
    prob = .5
    fractions_won, probs = [], []
    while prob <= 1:
        fractions_won.append(fraction_won(prob, num_series, 7))
        probs.append(prob)
        prob += .01
    matplotlib.use('TkAgg')
    plt.axhline(0.95)
    plt.plot(probs, fractions_won, 'k', linewidth=5)
    plt.xlabel('Probability of Winning a Game')
    plt.ylabel('Probability of Wining a Series')
    plt.title(f'{num_series} Seven-Game Series')
    plt.savefig(f'sim{num_series}-7game-series')
    plt.show()


if __name__ == '__main__':
    sim_series(400)
