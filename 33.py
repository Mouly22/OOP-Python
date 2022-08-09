class Author:
    def __init__(self,*infs):
        if len(infs) == 0:
            self.name = 'Default'
            self.bks = []
        elif len(infs) == 1:
            self.name = infs[0]
            self.bks = []
        else:
            self.name = infs[0]
            self.bks = infs[1::]
            self.bks = list(self.bks)


        
        
    def addBooks(self, *books):
        for p in books:
            self.bks.append(p)
            
    def changeName(self, name):
        self.name = name
        
    def printDetails(self):
        print(f'Author Name: {self.name}')
        print('--------')
        print('List of Books:')
        for i in self.bks:
            print(i)

            
            
auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print('===================')
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
print('===================')
auth2.printDetails()
print('===================')
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()