class Student:
    ID = 0
    def __init__(self, name, dept, age, cg):
        self.name = name
        self.dept = dept
        self.age = age
        self.cg = cg
        Student.ID += 1
        
        
    def get_details(self):
        print(f'ID: {Student.ID} \nName: {self.name} \nDepartment: {self.dept} \nAge: {self.age} \nCGPA: {self.cg}')
        
    @classmethod
    def from_String(cls, val):
        name, dept, age, cg = val.split('-')
        obj = cls(name, dept, age, cg)
        return obj






s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()