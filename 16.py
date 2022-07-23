class Shape:
    def __init__(self, size, a, b):
        self.size = size
        self.a = a
        self.b = b

    def area(self):
        if self.size == "Square":
            area = self.a * self.b
            print(f"Area: {area}")
        elif self.size == "Triangle":
            area = (self.a * self.b)/2
            print(f"Area: {area}")
        elif self.size == "Rhombus":
            area =  (self.a * self.b)/2
            print(f"Area: {area}")
        elif self.size == "Rectangle":
            area =  (self.a * self.b)
            print(f"Area: {area}")
        else:
            print("Area: Shape Unknown")

triangle = Shape("Triangle",10,25)
triangle.area()
print("==========================")
square = Shape("Square",10,10)
square.area()
print("==========================")
rhombus = Shape("Rhombus",18,25)
rhombus.area()
print("==========================")
rectangle = Shape("Rectangle",15,30)
rectangle.area()
print("==========================")
trapezium = Shape("Trapezium",15,30)
trapezium.area()