class box:
    def __init__(self, lst):
        print('Creating a Box!')
        for i in range(len(lst)):
            self.height = lst[0] 
            self.width = lst[1]
            self.breadth = lst[2]
        a = self.height * self.width * self.breadth
            
        print(f"Volume of the box is {a} cubic units.")
            
print("Box 1")
b1 = box([10,10,10])
print("=========================")
print("Height:", b1.height)
print("Width:", b1.width)
print("Breadth:", b1.breadth)
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print("=========================")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
print("-------------------------")
print("Box 3")
b3 = b2
print("Height:", b3.height)
print("Width:", b3.width)
print("Breadth:", b3.breadth)
