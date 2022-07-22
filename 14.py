class Course:
    def __init__(self, name, faculty, time):
        self.name = name
        self.faculty = faculty
        self.time = time
    def detail(self):
        print(f'{self.name} - {self.faculty} - {self.time}')      
        
c1 = Course("CSE110", "TBA", 8)
c1.detail()
print("===============")
c2 = Course("CSE111", "TBA", 9)
c2.detail()