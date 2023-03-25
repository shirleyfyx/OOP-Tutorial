class Employee:

    raise_amt = 1.00
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def email(self):
        return '{}.{} @email.com'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.first = None

    
emp_1 = Employee('Shirley', 'Fang', 5000)

emp_1.fullname = 'Test User'

del emp_1.fullname

#emp_1.first = 'Jim'
# Need to update the email automatically. 

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
