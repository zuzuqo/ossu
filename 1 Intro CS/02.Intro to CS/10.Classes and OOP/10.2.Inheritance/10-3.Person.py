import datetime


class Person(object):
    def __init__(self, name):
        self._name = name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank + 1:]
        except:
            self._last_name = name
        self.birthday = None

    def get_name(self):
        return self._name

    def get_last_name(self):
        return self._last_name

    def set_birthday(self, birthdate):
        self._birthday = birthdate

    def get_age(self):
        if self._birthday == None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days

    def __lt__(self, other):
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name

    def __str__(self):
        return self._name


class MITPerson(Person):
    _next_id_num = 0

    def __init__(self, name):
        super().__init__(name)
        self._id_num = MITPerson._next_id_num
        MITPerson._next_id_num += 1

    def get_id_num(self):
        return self._id_num

    def __lt__(self, other):
        return self._id_num < other._id_num

    def is_student(self):
        return isinstance(self, Student)


class Politician(Person):
    def __init__(self, name, party=None):
        super().__init__(name)
        self.party = party

    def get_party(self):
        return self.party

    def might_agree(self, other_parties):
        if self.party is None or None in other_parties or self.party.lower() in map(lambda x: x.lower(), other_parties):
            return True
        else:
            return False


class Student(MITPerson):
    pass


class UG(Student):
    def __init__(self, name, class_year):
        super().__init__(name)
        self.year = class_year

    def get_class(self):
        return self.year


class Grad(Student):
    pass


class TransferStudent(Student):
    def __init__(self, name, from_school):
        MITPerson.__init__(self, name)
        self._from_school = from_school

    def get_old_school(self):
        return self._from_school


p1 = MITPerson('Barbara Beaver')
p2 = MITPerson('Petter Freeman')
print(f"{p1}'s id number is {p1.get_id_num()}")
print(f"{p2}'s id number is {p2.get_id_num()}")

p1 = Politician('Barbara Streisand', 'IT specialists')
p2 = Politician('John Dorian', 'it specialists')
p3 = Politician('Mark Brown', 'IT nya')
p4 = Politician('Clark Kent')
print(f"p1 and p2 might agree in politic is {p1.might_agree([p2.get_party()])}")
print(f"p1 and p3 might agree in politic is {p1.might_agree([p3.get_party()])}")
print(f"p1 and p2 might agree in politic is {p1.might_agree([p4.get_party()])}")

p4 = MITPerson('Clark Kent')

p5 = Grad('Buzz Lighter')
p6 = UG('Eugene Crabs', 1984)
print(f"{p5} is a graduate student is {type(p5) == Grad}")
print(f"{p5} is a undergraduate student is {type(p5) == UG}")

print(f"{p5} is a student is {p5.is_student()}")
print(f"{p6} is a student is {p6.is_student()}")
print(f"{p4} is a student is {p4.is_student()}")
