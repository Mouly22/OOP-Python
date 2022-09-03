class Author:
    def __init__(self, name = None):
        self.name = name
        self.bnlst = []
        self.btlst = []
        
    def addBook(self, bname, btyp):
        self.bname = bname
        self.btyp = btyp
        if self.name == None:
            print('A book can not be added without author name')
        else:
            self.bnlst.append(self.bname)
            self.btlst.append(self.btyp)
        
    def setName(self, name):
        self.name = name
        
    def printDetail(self):
        print(f'Number of Book(s): {len(self.bnlst)}')
        print(f'Author Name: {self.name}')
        for i in range(len(self.bnlst)):
            print(f'{self.btlst[i]}:{self.bnlst[i]}')
        

a1 = Author()
print("=================================")
a1.addBook('Ice', 'Science Fiction')
print("=================================")
a1.setName('Anna Kavan')
a1.addBook('Ice', 'Science Fiction')
a1.printDetail()
print("=================================")
a2 = Author('Humayun Ahmed')
a2.addBook('Onnobhubon', 'Science Fiction')
a2.addBook('Megher Upor Bari', 'Horror')
print('=================================')
a2.printDetail()
a2.addBook('Ireena', 'Science Fiction')
print("=================================")
a2.printDetail()
print("=================================")