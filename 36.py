class StudentDatabase:
    def __init__(self, name, iD):
        self.name = name
        self.iD = iD
        self.grades = {}
        self.sem = None
        self.courses = []
        
    def calculateGPA(self, lst, sem="Summer2022"):
        dct = {}
        dct1 = {}
        self.lst = lst
        total = 0
        count = 0
        for i in range(len(lst)):
            a = lst[i].split(': ')
            key = a[0].strip()
            value = a[1].strip()
            dct[key] = value
            total += float(value)
            count += 1
        total = total /count
        total = round(total,2)
        keytup = []
        for i in dct.keys():
            self.courses.append(i)
            keytup.append(i)
        keytup = tuple(keytup)
        self.grades[sem] = {keytup:total}
        self.sem = sem
        #print(dct)

        
        
    
    def printDetails(self):
        print(f'Name: {self.name}')
        print(f'ID: {self.iD}')

        for key,val in self.grades.items():
            print(f'Courses taken in {key}:')
            for k,v in val.items():
                for elm in k:
                    print(elm)
                print(f"GPA: {v}")

s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'],
'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'],
'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()