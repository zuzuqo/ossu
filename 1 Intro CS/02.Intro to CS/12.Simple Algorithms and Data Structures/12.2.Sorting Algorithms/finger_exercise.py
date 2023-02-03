from merge_sort import merge_sort

if __name__ == '__main__':
    a = [(1, 5, 3, 2), (2, 3), (0, 1), (3, 5, 2)]
    print(merge_sort(a, lambda x, y: sum(x) < sum(y)))
