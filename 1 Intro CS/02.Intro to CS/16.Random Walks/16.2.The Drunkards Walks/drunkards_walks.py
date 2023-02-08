import random
from matplotlib import pyplot as plt
import matplotlib


class Location(object):
    def __init__(self, x: float, y: float):
        self._x, self._y = x, y

    def move(self, delta_x: float, delta_y: float):
        return Location(self._x + delta_x, self._y + delta_y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def dist_from(self, other):
        ox, oy = other.get_x(), other.get_y()
        x_dist, y_dist = self._x - ox, self._y - oy
        return (x_dist ** 2 + y_dist ** 2) ** 0.5

    def __str__(self):
        return f'<{self._x}, {self._y}>'


class Field(object):
    def __init__(self):
        self._drunks = {}

    def add_drunk(self, drunk, loc: Location):
        if drunk in self._drunks:
            raise ValueError('Duplicate drunk')
        else:
            self._drunks[drunk] = loc

    def move_drunk(self, drunk):
        if drunk not in self._drunks:
            raise ValueError('Drunk not in field')
        x_dist, y_dist = drunk.take_step()
        current_location = self._drunks[drunk]
        # new location
        self._drunks[drunk] = current_location.move(x_dist, y_dist)

    def get_loc(self, drunk):
        if drunk not in self._drunks:
            raise ValueError('Drunk not in field')
        return self._drunks[drunk]


class Drunk(object):
    def __init__(self, name=None):
        self._name = name

    def __str__(self):
        if self is not None:
            return self._name
        return 'Anonymous'


class UsualDrunk(Drunk):
    def take_step(self):
        step_choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(step_choices)


def walk(f: Field, d: UsualDrunk, num_steps: int):
    if num_steps < 0:
        return None
    start = f.get_loc(d)
    for s in range(num_steps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))


def sim_walks(num_steps: int, num_trials: int, d_class) -> list:
    homer = d_class()
    origin = Location(0, 0)
    distances = []
    for t in range(num_trials):
        f = Field()
        f.add_drunk(homer, origin)
        distances.append(round(walk(f, homer, num_steps), 1))
    return distances


def drunk_test(walk_lengths, num_trials, d_class):
    mean = []
    for num_steps in walk_lengths:
        distances = sim_walks(num_steps, num_trials, d_class)
        mean.append(sum(distances) / len(distances))
        print(f'{d_class.__name__} walk of {num_steps} steps: Mean = {sum(distances) / len(distances):.3f},'
              f'Max = {max(distances)}, Min = {min(distances)}')

    matplotlib.use('TkAgg')

    plt.figure('Mean Distance from Origin (100 trials)')
    plt.title('Mean Distance from Origin (100 trials)')
    plt.xlabel('Number of Steps')
    plt.ylabel('Distance from Origin')
    plt.plot(walk_lengths, mean)
    plt.show()





if __name__ == '__main__':
    drunk_test((10, 100, 1000, 10000), 100, UsualDrunk)


