class Student:
    def __init__(self, name = None, dept = None):
        self.name = name
        self.dept = dept
        if self.name == None and self.dept == None:
            print("Student name and department need to be set")
        elif self.dept == None:
            print(f'Department for {self.name} needs to be set')
        else:
            print(f'{self.name} is from {self.dept} department')
            
    def update_name(self, name):
        self.name = name
        
    def update_department(self, dept):
        self.dept = dept
        
    def enroll(self, *subs):
        lst = []
        for p in subs:
            lst.append(p)
        self.lst = lst
    def printDetail(self):
        print(f'{self.name} enrolled in {len(self.lst)} course(s):')
        for j in self.lst:
            print(j)
            
s1 = Student()
print('=========================')
s2 = Student('Carol')
print('=========================')
s3 = Student('Jon', 'EEE')
print('=========================')
s1.update_name('Bob')
s1.update_department('CSE')
s2.update_department('BBA')
s1.enroll('CSE110', 'MAT110', 'ENG091')
s2.enroll('BUS101')
s3.enroll('MAT110', 'PHY111')
print('###########################')
s1.printDetail()
print('=========================')
s2.printDetail()
print('=========================')
s3.printDetail()