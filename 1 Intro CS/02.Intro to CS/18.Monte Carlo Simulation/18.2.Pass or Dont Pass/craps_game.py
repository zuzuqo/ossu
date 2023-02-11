import random

import numpy as np


def roll_die(n=6):
    return random.choice(range(1, n + 1))


class CrapsGame(object):
    def __init__(self):
        self.pass_wins, self.pass_losses = 0, 0
        self.dp_wins, self.dp_losses, self.dp_pushes = 0, 0, 0

    def play_hand(self):
        throw = roll_die() + roll_die()
        if throw in [7, 11]:
            self.pass_wins += 1
            self.dp_losses += 1
        elif throw in [2, 3, 12]:
            self.pass_losses += 1
            if throw == 12:
                self.dp_pushes += 1
            else:
                self.dp_wins += 1
        else:
            point = throw
            while True:
                throw = roll_die() + roll_die()
                if throw == point:
                    self.pass_wins += 1
                    self.dp_losses += 1
                    break
                elif throw == 7:
                    self.pass_losses += 1
                    self.dp_wins += 1
                    break

    def pass_results(self):
        return self.pass_wins, self.pass_losses

    def dp_results(self):
        return self.dp_wins, self.dp_losses, self.dp_pushes


def craps_sim(hands_per_game, num_games):
    games = []
    for t in range(num_games):
        c = CrapsGame()
        for i in range(hands_per_game):
            c.play_hand()
        games.append(c)

    p_roi_per_game, dp_roi_per_game = [], []
    for g in games:
        wins, losses = g.pass_results()
        p_roi_per_game.append((wins - losses) / hands_per_game)
        wins, losses, pushes = g.dp_results()
        dp_roi_per_game.append((wins - losses) / hands_per_game)
    mean_roi = round(100 * sum(p_roi_per_game) / num_games, 4)
    sigma = round(100 * np.std(p_roi_per_game), 4)
    print(f'Pass: Mean ROI = {mean_roi}%, Std.Dev. = {sigma}%')
    mean_roi = round(100 * sum(dp_roi_per_game) / num_games, 4)
    sigma = round(100 * np.std(dp_roi_per_game), 4)
    print(f'Don\'t pass: Mean ROI = {mean_roi}%, Std.Dev. = {sigma}%')


if __name__ == '__main__':
    craps_sim(20, 10000)