class Int_set(object):
    '''An Int_set is a set of integers'''

    def __init__(self):
        self._vals = []

    def insert(self, e):
        '''Assumes e is an integer and inserts e into self'''
        if e not in self._vals:
            self._vals.append(e)

    def member(self, e):
        return e in self._vals

    def remove(self, e):
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def get_members(self):
        return self._vals[:]

    def __str__(self):
        if self._vals == []:
            return '{}'
        self._vals.sort()
        res = ''
        for e in self._vals:
            res += str(e) + ','
        return f'{{{res[:-1]}}}'

a = Int_set()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(-33)

print(a)