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


class ColdDrunk(Drunk):
    def take_step(self):
        step_choices = [(0, 1), (0, -2), (1, 0), (-1, 0)]
        return random.choice(step_choices)


class EWDrunk(Drunk):
    def take_step(self):
        step_choices = [(1, 0), (-1, 0)]
        return random.choice(step_choices)


class StyleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def next_style(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result


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


def sim_all(drunk_kinds, walk_lengths, num_trials):
    for d_class in drunk_kinds:
        drunk_test(walk_lengths, num_trials, d_class)


def sim_drunk(num_trials, d_class, walk_lengths):
    mean_distances = []
    for num_steps in walk_lengths:
        print(f'Starting simulation of {num_steps} steps')
        trials = sim_walks(num_steps, num_trials, d_class)
        mean = sum(trials) / len(trials)
        mean_distances.append(mean)
    return mean_distances


def sim_all_plot(drunk_kinds, walk_lengths, num_trials):
    style_choice = StyleIterator(('m-', 'r:', 'k-.'))
    matplotlib.use('TkAgg')

    for d_class in drunk_kinds:
        cur_style = style_choice.next_style()
        print(f'Starting simulation of {d_class.__name__}')
        means = sim_drunk(num_trials, d_class, walk_lengths)
        plt.plot(walk_lengths, means, cur_style, label=d_class.__name__)

    plt.title(f'Mean Distance from Origin {num_trials} trials')
    plt.xlabel('Number of Steps')
    plt.ylabel('Distance from Origin')
    plt.legend(loc='best')
    plt.semilogx()
    plt.semilogy()
    plt.savefig('drunk_distance')
    plt.show()


def get_final_locs(num_steps, num_trials, d_class):
    locs = []
    d = d_class()
    for t in range(num_trials):
        f = Field()
        f.add_drunk(d, Location(0, 0))
        for s in range(num_steps):
            f.move_drunk(d)
        locs.append(f.get_loc(d))
    return locs


def plot_locs(drunk_kinds, num_steps, num_trials):
    style_choice = StyleIterator(('k+', 'r^', 'mo'))
    matplotlib.use('TkAgg')

    for d_class in drunk_kinds:
        locs = get_final_locs(num_steps, num_trials, d_class)
        x_vals, y_vals = [], []
        for loc in locs:
            x_vals.append(loc.get_x())
            y_vals.append(loc.get_y())
        mean_x = sum(x_vals) / len(x_vals)
        mean_y = sum(y_vals) / len(y_vals)
        cur_style = style_choice.next_style()
        plt.plot(x_vals, y_vals, cur_style, label=f'{d_class.__name__} mean loc. = <{mean_x}, {mean_y}>')

    plt.title(f'Location an End of Walks ({num_steps} steps)')
    plt.xlabel('Steps East/West of Origin')
    plt.ylabel('Steps North/South of Origin')
    plt.legend(loc='best')
    plt.savefig('drunk-locs')
    plt.show()


def trace_walk(drunk_kinds, num_steps):
    matplotlib.use('TkAgg')

    f = Field()
    for d_class in drunk_kinds:
        d = d_class()
        f.add_drunk(d, Location(0, 0))
        locs = []
        for s in range(num_steps):
            f.move_drunk(d)
            locs.append(f.get_loc(d))
        x_vals, y_vals = [], []
        for loc in locs:
            x_vals.append(loc.get_x())
            y_vals.append(loc.get_y())
        plt.plot(x_vals, y_vals, label = d_class.__name__)
    plt.title(f'Spots Visited on Walk ({num_steps} steps)')
    plt.xlabel('Steps East/West of Origin')
    plt.ylabel('Steps North/South of Origin')
    plt.legend(loc='best')
    plt.savefig('drunk-trace')
    plt.show()


if __name__ == '__main__':
    drunks = [UsualDrunk, ColdDrunk, EWDrunk]
    steps = [10, 100, 1000, 10000, 100000]
    # sim_all_plot(drunks, steps, 100)
    # plot_locs(drunks, 100, 200)
    trace_walk(drunks, 200)
