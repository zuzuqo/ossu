import random

import numpy as np


def roll_die(n=6):
    return random.choice(range(1, n + 1))


class BigSix(object):
    def __init__(self):
        self.pass_wins, self.pass_losses = 0, 0

    def play_hand(self):
        throw = roll_die() + roll_die()
        if throw in [6]:
            self.pass_wins += 1
        elif throw in [7]:
            self.pass_losses += 1
        else:
            while True:
                throw = roll_die() + roll_die()
                if throw == 6:
                    self.pass_wins += 1
                    break
                elif throw == 7:
                    self.pass_losses += 1
                    break

    def pass_results(self):
        return self.pass_wins, self.pass_losses


def big_six_sim(hands_per_game, num_games):
    games = []
    for t in range(num_games):
        c = BigSix()
        for i in range(hands_per_game):
            c.play_hand()
        games.append(c)

    p_roi_per_game = []
    for g in games:
        wins, losses = g.pass_results()
        p_roi_per_game.append((wins - losses) / hands_per_game)

    print(f'Big Six Game Results')
    mean_roi = round(100 * sum(p_roi_per_game) / num_games, 4)
    sigma = round(100 * np.std(p_roi_per_game), 4)
    print(f'Pass: Mean ROI = {mean_roi}%, Std.Dev. = {sigma}%')


if __name__ == '__main__':
    big_six_sim(30, 10000)
