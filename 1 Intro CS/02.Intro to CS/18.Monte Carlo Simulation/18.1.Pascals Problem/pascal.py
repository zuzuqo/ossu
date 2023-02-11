import random


def roll_die():
    return random.choice([1, 2, 3, 4, 5, 6])


def check_pascal(num_trials):
    num_wins = 0
    ind = []
    for i in range(num_trials):
        for j in range(24):
            d1 = roll_die()
            d2 = roll_die()
            if d1 == d2 == 6:
                num_wins += 1
                ind.append(j)
                break
            if j == 23:
                ind.append(36)
    mean = sum(ind) / len(ind)
    print(f'Probability of winning = {num_wins / num_trials}\n'
          f'Mean index = {mean}')


if __name__ == '__main__':
    check_pascal(100000)
