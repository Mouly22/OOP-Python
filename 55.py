class Coordinates:
    def __init__(self, val1, val2):
        self.val1 =val1
        self.val2 = val2
        
    def __sub__(self, other):
        sub_val1 = self.val1 - other.val1
        sub_val2 = self.val2 - other.val2
        p4 = Coordinates(sub_val1, sub_val2)
        return p4
    
    def detail(self):
        return(self.val1, self.val2)
    
    def __mul__(self, other):
        mul_val1 = self.val1 * other.val1
        mul_val2 = self.val2 * other.val2
        p5 = Coordinates(mul_val1, mul_val2)
        return p5
       
  
    def __eq__(self, other):
        com_val1 = (self.val1 == other.val1)
        com_val2 = (self.val2 == other.val2)
        point_check = Coordinates(com_val1, com_val2)
        if (self.val1 == other.val1) and (self.val2 == other.val2) :
            point_check = 'The calculated coordinates are the same.'
        else:
            point_check = 'The calculated coordinates are NOT the same.'
        return point_check
        
        


p1 = Coordinates(int(input()),int(input()))
p2 = Coordinates(int(input()),int(input()))
p4 = p1 - p2
print(p4.detail())
p5 = p1 * p2
print(p5.detail())
point_check = (p4 == p5)
print(point_check)