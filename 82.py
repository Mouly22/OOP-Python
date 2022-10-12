class A:
    def __init__(self):
        self.temp = 4
        self.sum = 1
        self.y = 2
        self.y = self.temp - 2
        self.sum = self.temp + 3
        self.temp -= 2

    def methodA(self, m, n):
        x = 0
        self.y = self.y + m + self.temp
        self.temp += 1
        x = x + 2 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)

class B(A): 
    def __init__(self, b=None):
        super().__init__()
        self.x = 1
        self.sum = 2
        if b == None:
            self.y = self.temp + 3
            self.sum = 3 + self.temp + 2
            self.temp -= 1
        else:
            self.sum = b.sum
            self.x = b.x
            
    def methodB(self, m, n):
        y = 0
        y = y + self.y
        self.x = y + 2 + self.temp
        self.methodA(self.x, y)
        self.sum = self.x + y + self.sum
        print(self.x, y, self.sum)
        
a1 = A()
b1 = B()
b2 = B(b1)
a1.methodA(1, 1)
b1.methodA(1, 2)
b2.methodB(3, 2)