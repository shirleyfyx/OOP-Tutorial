# Python Object-Oriented Programming 

class Employee:

    raise_amt = 1.04

    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)
    
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Shirley', 'Fang', 5000)
emp_2 = Employee('Test', 'User', 6000)

import datetime
my_date = datetime.date(2023,1,1)

print(Employee.is_workday(my_date))

