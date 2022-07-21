class Calculator:
    def __init__(self, inp1,operator, inp2):
        self.inp1 = inp1
        self.inp2 = inp2
        self.operator = operator
        
        
    def add(self):
        if self.operator == "+":
            print("Result:", self.inp1 + self.inp2)
    def subtract(self):
        if self.operator == "-":
            print("Result:", self.inp1 - self.inp2)
    def multiply(self):
        if self.operator == "*":
            print("Result:", self.inp1 * self.inp2)            
    def divide(self):
        if self.operator == "/":
            print("Result:", self.inp1 / self.inp2)
print('Let’s Calculate!')    
inp1 = int(input("value1: "))
operator = input("Operator: ")
inp2 = int(input("value2: "))


obj1 = Calculator(inp1, operator, inp2)
obj1.add()
obj1.subtract()
obj1.multiply()
obj1.divide()

