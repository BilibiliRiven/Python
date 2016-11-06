import json


class Person(object):
    __count = 0

    @classmethod
    def how_many(cls):
        return cls.__count

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        Person.__count += 1

    def who_am_i(self):
        return "I am a person, my name is %s" % self.name


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        score = score

    def who_am_i(self):
        return "I am a student, my name is %s" % self.name


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

    def who_am_i(self):
        return "I am a teacher, my name is %s" % self.name


def whoami(x):
    return x.who_am_i()



#s = Students()
#p = Person('Tim', 'Male')
#s = Student('Bob', 'Male', 88)
#t = Teacher('Alice', 'Female', 'English')


# class Student(object):
#     def read(self):
#         return r'["Tim", "Bob", "Alice"]'


class SkillMixin(object):
    pass


class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'


class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'


class Bstudent(Student, BasketballMixin):
    def __int__(self, name, gender, score):
        super(Bstudent, self).__init__(name, gender, score)
        pass


class Fteacher(Teacher, FootballMixin):
    def __init__(self, name, gender, course):
        super(Fteacher,self).__init__(name, gender, course)
        pass

s = Bstudent("Bob", 'Female', 88)
print s.skill()

p = Fteacher('Lisa', 'Female', 'English')
print p.skill()



# s = Students()
# print json.load(s)

# print whoami(p)
# print whoami(s)
# print whoami(t)
# print Person.how_many()
# p1 = Person("Bob")
# print Person.how_many()