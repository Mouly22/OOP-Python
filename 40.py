class ShoppingCart:
    def __init__(self, cname = None):
        self.cname = cname
        self.dct = {}
        
    def addGadget(self, *products):
        if self.cname != None:
            for elms in products:
                self.dct[elms.gadget] = [elms.model, elms.price, elms.stock]        
        else:
            print('Please set the cart name first.')
            
    def setCartName(self, cname = None):
        self.cname = cname
        
    def printCartDetails(self):
        if self.cname != None:
            print(f'Details of {self.cname}')
            print(f'Total gadgets in cart: {len(self.dct.keys())}')     
            for m, n in self.dct.items():
                print(f'Gadget: {m} Model: {n[0]} BlackShark Price: {n[1]}\$ Stock: {n[2]} pcs')
        else:
            print('Please set the cart name first.')
            
    def removeFromCart(self, gadget):
        self.gadget = gadget
        if gadget not in self.dct.keys():
            print(f'{gadget} not found in cart!')
        else:
            del self.dct[gadget]
            print(f'{self.gadget} removed from cart!')   
    
class Product:  
    def __init__(self, gadget, model, price, stock):
        self.gadget = gadget
        self.model = model
        self.price = price
        self.stock = stock

s1 = ShoppingCart()
p1 = Product("Razer BlackShark","Headset",99.99,5)
p2 = Product("Razer Huntsman","Keyboard", 249.99,12)
print("1.====================================")
s1.addGadget(p1,p2)
print("2.====================================")
s1.setCartName("Amazon")
s1.addGadget(p1,p2)
s1.addGadget(Product("HyperX Fury", "Mousepad",26.99,21))
print("3.====================================")
s1.printCartDetails()
print("4.====================================")
s1.removeFromCart("Logitech G ProX Superlight")
print("5.====================================")
s1.removeFromCart("Razer Huntsman")
print("6.====================================")
s1.printCartDetails()