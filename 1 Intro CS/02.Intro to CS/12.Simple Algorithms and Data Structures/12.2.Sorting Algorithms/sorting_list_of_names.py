from merge_sort import merge_sort

def last_name_first_name(name1: str, name2: str):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[1] != arg2[1]:
        return arg1[1] < arg2[1]
    else:
        # last name the same, sort by fst name
        return arg1[0] < arg2[0]


def first_name_last_name(name1: str, name2: str):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[0] != arg2[0]:
        return arg1[0] < arg2[0]
    else:
        # last name the same, sort by fst name
        return arg1[1] < arg2[1]


if __name__ == '__main__':
    L = ['Kenny McCormick', 'Eric Cartman', 'Kyle Broflovski', 'Clyde Donovan', 'Jimmy Valmer', 'Stan March',
         'Craig Tucker']

    new_L = merge_sort(L, last_name_first_name)
    print(f'Sorted by last name:\t{new_L}')
    new_L = merge_sort(L, first_name_last_name)
    print(f'Sorted by first name:\t{new_L}')
