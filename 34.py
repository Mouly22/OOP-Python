class TaxiLagbe:
    def __init__(self, date, place):
        self.date = date
        self.place = place
        self.totalpassenger = 0
        self.lst = []
        self.totalmoney = 0
        
    def addPassenger(self, *name):  
        if self.totalpassenger < 4:
            for i in name:
                a = i.split("_")
                name = a[0]
                price = a[1]
                self.totalmoney += int(price)
                print(f'Dear {name}! Welcome to TaxiLagbe.')
                self.totalpassenger += 1
                self.lst.append(name)
        else:
            print("Taxi Full! No more passengers can be added.")      
            
    def printDetails(self):
        print(f'Trip info for Taxi number: {self.date}')
        print(f'This taxi can cover only {self.place} area.')
        print(f"Total passengers {self.totalpassenger}")
        print(f"Passenger lists:")
        sum1 = ""
        for i in self.lst:
            sum1 += i + ', '
        sum1 = sum1.strip(", ")
        print(sum1)
        print(f"Total collected fare {self.totalmoney} Taka")     
        
taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200')
taxi1.addPassenger('Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115')
taxi2.addPassenger('Parker_215')
print('-------------------------------')
taxi2.printDetails() 