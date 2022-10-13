class Student:
    count = 0

    @classmethod
    def CreateStudent(cls,  name= 'Unknown', dept= 'CSE', cgpa= 0):
        print('Student1 Created with default parameters')
        cls.name = name
        cls.dept = dept
        cls.cgpa = cgpa
        obj = cls(name, dept, cgpa)
        return obj

     


    def __init__(self, name= 'Unknown', dept= 'CSE', cgpa= 0):
        self.name = name
        self.dept = dept
        self.cgpa = cgpa
        Student.count += 1
        self.stcount = Student.count

    def updateCGPA(self, cgpa):
        self.cgpa = cgpa

    def details(self):
        print(f'*********************************')
        print(f'Student{self.stcount}:')
        print(f'Name: {self.name}')
        print(f'Department:{self.dept}')
        print(f'CGPA:{self.cgpa}')

    @classmethod
    def compare(cls, v1, v2):
        if v1 > v2:
            print(f'{v1}> {v2}')
        else:
            print(f'{v2}> {v1}')

Student1 = Student.CreateStudent()
Student2 = Student('Karim','EEE')
Student3 = Student('Rahim','ECE')
Student1.details()
Student2.updateCGPA(3.33)
Student3.updateCGPA(3.1)
Student4 = Student('Sani','BBA',3.53)
Student2.details()
Student3.details()
Student.compare(3.22, 3.50)