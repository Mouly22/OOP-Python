class Cat:
    Number_of_cats = 0
    @classmethod
    def no_parameter(cls):
        obj = cls('White', 'sitting')
        return obj
    @classmethod
    def first_parameter(cls,color):
        obj = cls(color, 'sitting')
        return obj
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        Cat.Number_of_cats += 1
        
    @classmethod
    def second_parameter(cls, pos):
        obj = cls('Grey', pos)
        return obj
            
    def printCat(self):
        print(f'Name: {self.color} cat is {self.pos}')
        
    def changeColor(self,color):
        self.color = color
    
print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)