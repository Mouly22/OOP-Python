class Student:
    def __init__(self, name, iD, prof = 'CSE'):
        self.name = name
        self.iD = iD
        self.prof = prof
        
    def dailyEffort(self, hr):
        self.hr = hr
        
        
    def printDetails(self):
        if self.hr <= 2:
            msg = 'Suggestion: Should give more effort!'
        elif self.hr <= 4:
            msg = 'Suggestion: Keep up the good work!'
        else:
            msg = 'Suggestion: Excellent! Now motivate others.'
            
        print(f'Name: {self.name}')
        print(f'ID: {self.iD}')
        print(f'Department: {self.prof}')
        print(f'Daily Effort: {self.hr} hour(s)')
        print(msg)
    
    
harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()