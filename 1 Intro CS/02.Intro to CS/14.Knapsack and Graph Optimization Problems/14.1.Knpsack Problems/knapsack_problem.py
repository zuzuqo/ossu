class Item(object):
    def __init__(self, name, value, weight):
        self._name = name
        self._value = value
        self._weight = weight

    def get_name(self):
        return self._name

    def get_value(self):
        return self._value

    def get_weight(self):
        return self._weight

    def __str__(self):
        return f"<{self._name}, {self._value}, {self._weight}>"


def build_items(names:[str]=None, values:[int]=None, weights:[int]=None):
    if names and values and weights is None:
        names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
        values = [175, 90, 20, 50, 10, 200]
        weights = [10, 9, 4, 2, 1, 20]
    items = []
    for i in range(len(names)):
        items.append(Item(names[i], values[i], weights[i]))
    return items


def gen_powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]


# algorithm
# 0/1 knapsack problem
def choose_best(pset, max_weight, get_val, get_weight):
    best_val = 0
    best_set = None
    for items in pset:
        items_val = 0
        items_weight = 0
        for item in items:
            items_val += get_val(item)
            items_weight += get_weight(item)
        if items_weight <= max_weight and items_val > best_val:
            best_val = items_val
            best_set = items
    return best_set, best_val


def test_best(max_weight=20):
    items = build_items()
    pset = gen_powerset(items)
    taken, val = choose_best(pset, max_weight, Item.get_value, Item.get_weight)
    print(f'Total value of items taken is {val}')
    for item in taken:
        print(item)


if __name__ == '__main__':
    test_best()
