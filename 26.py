class Student:
    def __init__(self, name = 'default student', score = 0):
        self.name = name
        self.score = score
        
    def quizcalc(self, *nums):
        sum = 0
        for i in nums:
            sum += i
            self.score = sum / 3

        
            
    def printdetail(self):
        print(f'Hello {self.name}')
        print(f"Your average quiz score is {self.score}")
        
s1 = Student()
s1.quizcalc(10)
print('--------------------------------')
s1.printdetail()
s2 = Student('Harry')
s2.quizcalc(10,8)
print('--------------------------------')
s2.printdetail()
s3 = Student('Hermione')
s3.quizcalc(10,9,10)
print('--------------------------------')
s3.printdetail()