class Toy(object):
    def __init__(self):
        self._elems = []

    def add(self, new_elems):
        '''new_elems is a list'''
        self._elems += new_elems

    def size(self):
        return len(self._elems)


print(type(Toy))
print(type(Toy.__init__), type(Toy.add), type(Toy.size))

t1 = Toy()
print(type(t1), type(t1.add))

t2 = Toy()

print(f't1 is t2: {t1 is t2}')

t1.add([3, 4])
t2.add([4])
print(f't1 size: {t1.size()}')
print(f't2 size: {t2.size()}')

print(f't1.size() + t2.size(): {t1.size() + t2.size()}')

