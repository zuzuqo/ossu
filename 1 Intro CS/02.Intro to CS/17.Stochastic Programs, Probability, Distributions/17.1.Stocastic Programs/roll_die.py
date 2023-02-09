import random


def roll_die(n: int = 6):
    '''Returns a random int between 1 and n'''
    return random.choice(range(1, n + 1))


def thrower(num_throws: int, n: int = 6):
    result = []
    for i in range(num_throws):
        result.append(roll_die(n))
    print(result)



if __name__ == '__main__':
    thrower(120)
