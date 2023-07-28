import datetime


class Person:
    type = 'human'

    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def get_description(self):
        return f"Hi! My name is {self.name}"

    def get_birth_year(self):
        return datetime.datetime.now().year - self.age

    @staticmethod
    def get_class_information():
        return f"Super class Person bla bla"


class Worker(Person):
    def __init__(self, name, age, gender, height, position, salary):
        super().__init__(name, age, gender, height)
        self.position = position
        self.salary = salary

    # override super-class method
    def get_description(self):
        return f"Hi! my name is {self.name}. I'm {self.age} years old"

    def get_work_info(self):
        return {
            'salary_d': self.salary / 21,
            'salary_m': self.salary,
            'salary_y': self.salary * 12
        }


# diamond inheritance
class Engineer(Worker):
    def __init__(self, name, age, gender, height, position, salary, occupation, experience):
        super().__init__(name, age, gender, height, position, salary)
        self.occupation = occupation
        self.experience = experience

    # random tax calculation
    def get_salary_tax(self):
        return {
            'tax_m': self.salary / (self.experience * 1) * 0.1,
            'tax_y': self.salary / (self.experience * 12) * 0.1,
        }


# inheritance
roman = Engineer(name='Roman',
                 age=33,
                 gender='male',
                 height=192,
                 position='Engineer',
                 salary=33800,
                 occupation='Embedded Engineer',
                 experience=12)

print(roman.get_salary_tax())

print(Engineer.get_class_information())
