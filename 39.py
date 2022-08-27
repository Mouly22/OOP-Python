class Student:
    def __init__(self, name, idd, dept):
        self.name = name
        self.idd = idd
        self.dept = dept
        
    def details(self):
        print(f'Name:{self.name}')
        print(f'ID:{self.idd}')
        return(f'Department:{self.dept}')
        
    def advise(self, *subs):
        g = ''
        for i in subs:
            a = len(i) * 3.0
            g = 'List of courses:' + i + ', '
            g = g.rstrip(', ')
        print(f'{self.name}, you have taken {a} credits.')
        print(g)     
        for i in subs:
            a = len(i) * 3.0
            if a == 6.0:
                print('You have to take at least 1 more course.')
            elif a == 9.0:
                print('Ok')
            elif a == 15.0:
                print('You have to drop at least 1 course.')
        
s1 = Student('Alice','20103012','CSE')
s2 = Student('Bob', '18301254','EEE')
s3 = Student('Carol', '17101238','CSE')
print('##########################')
print(s1.details())
print('##########################')
print(s2.details())
print('##########################')
s1.advise('CSE110', 'MAT110', 'PHY111')
print('##########################')
s2.advise('BUS101', 'MAT120')
print('##########################')
s3.advise('MAT110', 'PHY111', 'ENG102','CSE111', 'CSE230')