import random

from decision_tree import fast_max_val
from Item import Item


def small_test(func):
    names = ['a', 'b', 'c', 'd']
    vals = [7, 8, 4, 6]
    weights = [3, 4, 1, 5]
    items = []
    for i in range(len(vals)):
        items.append(Item(names[i], vals[i], weights[i]))
    val, taken = func(items, 5)
    for i in taken:
        print(i)
    print(f'Total value of items taken is {val}')


def build_many_items(num_items, max_value, max_weight):
    items = []
    for i in range(num_items):
        items.append(Item(str(i), random.randint(1, max_value), random.randint(1, max_weight)))
    return items


def big_test(func, num_items, avail_weight):
    items = build_many_items(num_items, 10, 10)
    val, taken = func(items, avail_weight)
    print('Items Taken')
    for i in taken:
        print(i)
    print(f'Total value of items taken is {val}')


if __name__ == '__main__':
    # small_test(fast_max_val)
    # big_test(fast_max_val, 10, 40)
    big_test(fast_max_val, 40, 100)
