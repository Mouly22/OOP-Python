class RealNumber:
    def __init__(self, r=0):
        self.__realValue = r
        
    def getRealValue(self):
        return self.__realValue
    
    def setRealValue(self, r):
        self.__realValue = r
        
    def __str__(self):
        return 'RealPart: '+str(self.getRealValue())

class ComplexNumber(RealNumber):
    def __init__(self, r = 1.0, r1 = 1.0):
        super().__init__(r = r)
        self.r = float(super().getRealValue())
        self.r1 = float(r1)
    def __str__(self):
        return f'Real Part: {str(self.r)} \nImaginary Part: {self.r1}'
    


cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5,7)
print(cn2)