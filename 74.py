class RealNumber:
    def __init__(self, number=0):
        self.number = number
    def __add__(self, anotherRealNumber):
        return self.number + anotherRealNumber.number
    def __sub__(self, anotherRealNumber):
        return self.number - anotherRealNumber.number
    def __str__(self):
        return str(self.number)
    
class ComplexNumber(RealNumber):
    def __init__(self, num, i):
        if type(num) == int:
            super().__init__(number = num)
        else:
            super().__init__(number = num.number)
        self.i = i
        
    def __str__(self):
        if self.i < 0:
            return f'{self.number} - {(-1)*self.i}i'
        else:
            return f'{self.number} + {self.i}i'
    
    def __add__(self, other):
        val1 = super().__add__(other)
        val2 = self.i + other.i
        obj = ComplexNumber(val1, val2)
        return obj
    
    def __sub__(self, other):
        val1 = super().__sub__(other)
        val2 = self.i - other.i
        obj = ComplexNumber(val1, val2)
        return obj
    
        
r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1+r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)
cn4 = cn1 - cn2
print(cn4)