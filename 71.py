class Shape:
    def __init__(self, name='Default', height=0, base=0):
        self.area = 0
        self.name = name
        self.height = height
        self.base = base
        self.area = 0.0
    def get_height_base(self):
        return "Height: "+str(self.height)+",Base: "+str(self.base)
    
    
    
class triangle(Shape):
    def __init__(self, name = 'Default', height =0, base = 0):
        super().__init__(name = name, height = height, base = base)
        
    def calcArea(self):
        self.area = 0.5 * self.height * self.base
        
    def printDetail(self):
        return(f'Shape name: {self.name} \nHeight: {self.height}, Base: {self.base} \nArea: {self.area}')
     
class trapezoid(Shape):
    def __init__(self, name, height, base, side_a):
        super().__init__(name = name, height = height, base = base)
        self.side_a = side_a
    def calcArea(self):
        self.area =  ((self.side_a + self.base)/2) * self.height
    def printDetail(self):
        return(f'Shape name: {self.name} \nHeight: {self.height}, Base: {self.base} Side_A: {self.side_a} \nArea: {self.area}')
         

#write your code here
tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())