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

emp_1 = Employee('Shirley', 'Fang', 5000)
emp_2 = Employee('Test', 'User', 6000)

emp_str_1 = 'Jon-Snow-7000'
emp_str_2 = 'Arya-Stark-8000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
#print(emp_str_1.email) 

#Employee.set_raise_amt(1.05)

#print(Employee.num_of_emps)

#print(emp_1.raise_amt)

#print(emp_1.email)
#print(emp_1.fullname())
#print(Employee.fullname(emp_2))

#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)
# print(Employee.apply_raise(emp_1)) 

#print(emp_1.__dict__)