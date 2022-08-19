class Dolls:
    def __init__(self, doll, price):
        self.doll = doll
        self.price = price
        self.flag = True
        
    def detail(self):
        if self.flag == True:
            return (f'Doll: {self.doll} \nTotal price: {self.price} taka')
        else:
            return (f'Dolls: {self.doll} \nTotal price: {self.price} taka')
        
    def __gt__(self, other):
        if self.price > other.price:
            return True
        else:
            return False

    def __add__(self, other):
        self.flag = False
        new_doll = self.doll +' '+ other.doll
        new_price = self.price + other.price
        obj_5 = Dolls(new_doll, new_price)
        obj_5.flag = False
        return obj_5


obj_1 = Dolls("Tweety", 2500)
print(obj_1.detail())
if obj_1 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_2 = Dolls("Daffy Duck", 1800)
print(obj_2.detail())
if obj_2 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_3 = Dolls("Bugs Bunny", 3000)
print(obj_3.detail())
if obj_3 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_4 = Dolls("Porky Pig", 1500)
print(obj_4.detail())
if obj_4 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_5 = obj_2 + obj_3
print(obj_5.detail())
if obj_5 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")