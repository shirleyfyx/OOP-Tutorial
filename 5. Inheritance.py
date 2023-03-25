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
    
class Developer(Employee):
    #Inherited from the Employee class.
    raise_amt = 1.50

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #or Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
    
dev_1 = Developer('Shirley', 'Fang', 5000, 'Python')
dev_2 = Developer('Test', 'User', 6000, 'Java')

mgr_1 = Manager('Sue','Smith',9000, [dev_1])

print(isinstance(mgr_1, Employee))
print(issubclass(Developer, Manager))

#print(mgr_1.email)
#mgr_1.add_emp(dev_2)
#mgr_1.print_emps()

#print(dev_1.prog_lang)
#print(dev_2.email)
#print(help(Developer))

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay) ???