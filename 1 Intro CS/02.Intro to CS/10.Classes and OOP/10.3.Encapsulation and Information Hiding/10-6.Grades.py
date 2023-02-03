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

class Grades(object):
    def __init__(self):
        '''
        Create empty grade book
        '''
        self._students = []
        self._grades = {}
        self._is_sorted = True

    def add_student(self, student):
        '''Assumes: student is of type Student
           Add student to the grade book'''
        if student in self._students:
            raise ValueError('Duplicate student')
        self._students.append(student)
        self._grades[student.get_id_num()] = []
        self._is_sorted = False

    def add_grade(self, student, grade):
        '''Assumes: grade is a float
           Add grade to the list of grades for student'''
        try:
            self._grades[student.get_id_num()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def get_grades(self, student):
        '''Return a list of grades for student'''
        try:
            return self._grades[student.get_id_num()][:]
        except:
            raise ValueError('Student not in mapping')

    def get_students(self):
        '''Return a sorted list of the students in the grade book'''
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True
        return self._students[:]


book = Grades()
book.add_student(Grad('Julie'))
book.add_student(Grad('Lisa'))
book.add_student(Grad('Anna'))
book.add_student(Grad('Pam'))


for s in book.get_students():
    print(s)
