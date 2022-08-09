class Dominos:
    def __init__(self, company):
        self.company = company
        print('Domino’s. The Pizza Delivery Experts.')
        self.dct = {}
        self.count = 0
        self.tcount = 0
        
    def addPizza(self, *others):
        for elm in others:
            self.count += 1
            vals = elm.lst[0].split(" ")
            types = vals[1]
                
            if types not in self.dct.keys():
                self.dct[types] = {elm.p_name : elm.lst}
            else:
                if elm.p_name not in self.dct[types]:
                    self.dct[types][elm.p_name] = elm.lst
        
    def showMenu(self):
        print(f'Total number of pizzas:{self.count}')
        
        for m, n in self.dct.items():
            print(f'{m} pizza: {len(n)}')
            for r, s in n.items():
                print(f'Name:{r}, Toppings: {s}')
            
class Pizza:
    def __init__(self, *items):

        self.lst = []
        if len(items) == 1:
            print('A pizza without toppings cannot be created.')
            self.p_name = items[0]
            self.lst = []
            
        else:
            self.p_name = items[0]
            for k in range(1,len(items)):
                self.lst.append(items[k])
                   
    def setToppings(self, *items1):
        for i in items1:
            self.lst.append(i)
        print(f'Toppings added to {self.p_name}')
        
        
#Write your code here
dom = Dominos("Domino's Pizza")
print("1.=================================")
p1 = Pizza("Spicy Chicken","Spicy Chicken","Onion","Capsicum")
dom.addPizza(p1)
p2 = Pizza("Margherita","Mozzarella Cheese")
print("2.=================================")
p3 = Pizza("Beef Kala Bhuna")
print("3.=================================")
p3.setToppings("Curried Beef","Capsicum","Paprika","Onion")
print("4.=================================")
dom.addPizza(p2,p3)
p4 = Pizza("Chicken Dominator","Barbecue Chicken", "Spicy Chicken","Grilled Chicken")
p5 = Pizza("Beefzza","Minced Beef","Beef Pepperoni","Onion","Jalapeno")
dom.addPizza(p4,p5)
print("5.=================================")
dom.showMenu()
print("6.=================================")