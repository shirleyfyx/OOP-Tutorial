class Employee:

    raise_amt = 1.00
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}',{})".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)
    
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Shirley', 'Fang', 5000)
emp_2 = Employee ('Test', 'User', 6000)

print(len(emp_1))

print('test'.__len__())
#print(emp_1 + emp_2)
# Because of the dunder add method. Read the documentation. 

#print(emp_1)
#print(repr(emp_1))
#print(emp_1.__repr__())
#str(emp_1)

# print(int.__add__(1, 2))
# print(str.__add__('a', 'b'))
# print('a'+'b')
