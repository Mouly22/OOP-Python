class Calculator:
    def __init__(self):
        self.v1 = 0
        self.v2 = 0
        self.sign = ''
        print('Calculator is ready!')


    def calculate(self, v1, v2, sign):
        self.v1 = v1
        self.v2 = v2
        self.sign = sign
        
        if self.sign == "+":
            return self.v1 + self.v2
        elif self.sign == "-":
            return self.v1 - self.v2
        elif self.sign == "*":
            return self.v1 * self.v2
        elif self.sign == "/":
            return self.v1 / self.v2
    
    def showCalculation(self):
        print(f'{self.v1} {self.sign} {self.v2} = {val}')


c1 = Calculator()
print("==================")
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 10, '-')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 5, '*')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 16, '/')
print("Returned value:", val)
c1.showCalculation()