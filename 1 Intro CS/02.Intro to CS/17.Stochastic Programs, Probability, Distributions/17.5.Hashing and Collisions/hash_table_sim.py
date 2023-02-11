import random


def collision_prob(n, k):
    prob = 1
    for i in range(1, k):
        prob *= (n - i) / n
    return 1 - prob


def sim_insertions(num_indices, num_insertions):
    choices = range(num_indices)
    used = []
    for i in range(num_insertions):
        hash_val = random.choice(choices)
        if hash_val in used:
            return 1
        else:
            used.append(hash_val)
    return 0


def find_prob(num_indices, num_insertions, num_trials):
    collisions = 0
    for t in range(num_trials):
        collisions += sim_insertions(num_indices, num_insertions)
    return collisions / num_trials


if __name__ == '__main__':
    print(f'Actual probability of a collision(1000, 50) = {collision_prob(1000, 50)}')
    print(f'Est. probability of a collision(1000, 50) = {find_prob(1000, 50, 10000)}')
    print(f'Actual probability of a collision(1000, 200) = {collision_prob(1000, 200)}')
    print(f'Est. probability of a collision(1000, 200) = {find_prob(1000, 200, 10000)}')
