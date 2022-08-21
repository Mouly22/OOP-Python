class Color:
    def __init__(self, clr):
        self.clr = clr
        
        
        
    def __add__(self, other):
        if (self.clr == 'red' and other.clr == 'yellow') or (self.clr == 'yellow' and other.clr == 'red'):
            res = 'Orange'
            C3 = Color(res)
        elif (self.clr == 'red' and other.clr == 'blue') or (self.clr == 'blue' and other.clr == 'red'):
            res = 'Violet'
            C3 = Color(res)
        elif (self.clr == 'yellow' and other.clr == 'blue') or (self.clr == 'blue' and other.clr == 'yellow'):
            res = 'Green'
            C3 = Color(res)
        return C3


C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)