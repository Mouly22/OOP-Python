class UberEats:
    def __init__(self,name,num,adrs):
        self.name = name
        self.num = num
        self.adrs = adrs
        self.orderlst = {}
        self.paid = 0
        print(f"{self.name}, welcome to UberEats!")
    def add_items(self,*args):
        lim = len(args)//2
        ornamelst = args[:lim]
        orpricelst = args[lim:]
        self.paid += sum(orpricelst)
        for i in range(len(ornamelst)):
            self.orderlst[ornamelst[i]] = orpricelst[i]
    def print_order_detail(self):
        print(f"User details: Name: {self.name}, Phone: {self.num}, Address: {self.adrs}")
        print(f"Orders: {self.orderlst}")
        return(f"Total Paid Amount: {self.paid}")

order1 = UberEats("Shakib", "01719658xxx", "Mohakhali")
print("=========================")
order1.add_items("Burger", "Coca Cola", 220, 50)
print("=========================")
print(order1.print_order_detail())
print("=========================")
order2 = UberEats ("Siam", "01719659xxx", "Uttara")
print("=========================")
order2.add_items("Pineapple", "Dairy Milk", 80, 70)
print("=========================")
print(order2.print_order_detail())