class Exam:
    def __init__(self,marks):
        self.marks = marks
        self.time = 60
        
    def examSyllabus(self):
        return "Maths , English"
    
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"
    
class ScienceExam(Exam):
    def __init__(self, marks, time, *args):
        self.lst = []
        super().__init__(marks = marks)
        self.time = time
        for i in args:
            self.lst.append(i)
            
    def __str__(self):
        return f'Marks: {self.marks} Time: {self.time} minutes Number of Parts: {2 + len(self.lst)}'
    
    def examSyllabus(self):
        for x in self.lst:
            val = x + ', '
        val = val.rstrip(', ')
        return f'{super().examSyllabus(), val}'
    
    def examParts(self):
        clst = []
        count = 3
        for g in self.lst:
            count += 1
            clst.append(count)
        well = ''   
        for x in range(len(self.lst)):
            well += 'Part' + str(x+3) + '-' + self.lst[x] + '\n'
            
        return f'{super().examParts()}{well}'
            
            
        
engineering = ScienceExam(100,90,"Physics","HigherMaths") 
print(engineering) 
print('----------------------------------') 
print(engineering.examSyllabus()) 
print(engineering.examParts()) 
print('==================================')
architecture = ScienceExam(100,120,"Physics","HigherMaths","Drawing") 
print(architecture) 
print('----------------------------------') 
print(architecture.examSyllabus()) 
print(architecture.examParts())