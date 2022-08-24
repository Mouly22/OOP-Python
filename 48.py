class Marks:
    def __init__(self, mark):
        self.mark = mark
        
    def __add__(self, other):
        total = Marks(self.mark + other.mark)
        return total
    
    
Q1 = Marks(int(input("Quiz 1 (out of 10): ")))
Q2 = Marks(int(input("Quiz 2 (out of 10): ")))
Lab = Marks(int(input("Lab (out of 30): ")))
Mid = Marks(int(input("Mid (out of 20): ")))
Final = Marks(int(input("Final (out of 30): ")))
total = Q1 + Q2 + Lab + Mid + Final
print("Total marks: {}".format(total.mark))