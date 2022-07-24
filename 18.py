class Student:
    def __init__(self, name, Id, dept, cg):
        self.name = name
        self.Id = Id
        self.dept = dept
        self.cg= cg
        
        
    def calculate_CGPA(self):
        total = 0 
        count = 0
        for i in self.cg:
            total += i
            count += 1
            
        self.CGPA = (total * 3) / (count * 3)
        self.CGPA = round(self.CGPA,2)
        
        
    
    def print_details(self):
        if self.CGPA > 3.8:
            msg = 'Your academic standing is \'Highest Distinction\''
        elif self.CGPA > 3.65:
            msg = 'Your academic standing is \'High Distinction\''
        elif self.CGPA > 3.50:
            msg = 'Your academic standing is \'Distinction\''
        elif self.CGPA > 2.00:
            msg = 'Your academic standing is \'Satisfactory\''
        else:
            msg = 'Sorry, you cannot graduate'
      
  
        print(f'Name: {self.name}, ID: {self.Id}')
        print(f'Department: {self.dept}')
        print(f'CGPA:{self.CGPA}')
        print(f'{msg}')
    
    
s1 = Student('Dora', '15995599','CSE', [4,3.7,3.7,4])
s1.calculate_CGPA()
print("==========================")
s1.print_details()
print("==========================")
s2 = Student('Pingu', '12312322', 'EEE', [1.7,1.3,1.3,1.3,1])
s2.calculate_CGPA()
print("==========================")
s2.print_details()
print("==========================")
s3 = Student('Bob', '13311331', 'CSE', [2,3,3,3.7,2.7,2.7])
s3.calculate_CGPA()
print("==========================")
s3.print_details()