class Student:
    t_stu = 0
    b_stu = 0
    o_stu = 0
    @classmethod
    def printDetails(self):
        print(f'Total Student(s): {Student.t_stu} \nBRAC University Student(s): {Student.b_stu} \nOther Institution Student(s): {Student.o_stu}')
        
    def __init__(self, name, dept, uni = 'BRAC University'):
        self.name = name
        self.dept = dept
        self.uni = uni
        Student.t_stu += 1
        if uni == 'BRAC University':
            Student.b_stu += 1
        else:
            Student.o_stu += 1
            
    def individualDetail(self):
        print(f'Name:{self.name} \nDepartment:{self.dept} \nInstitution: {self.uni}')
        
    @classmethod
    def createStudent(cls, name, dept, uni = 'BRAC University'):
        obj = cls(name, dept, uni)
        return obj


Student.printDetails()
print('#########################')
mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()
print('========================')
harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()
print('=========================')
levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()