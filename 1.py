class University:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
        
    def payment(self):
        print('Payment is done')
        print(f'{self.name}, {self.year}')
        
mouly = University('BRACU', 2020)
fahad = University('BRACU', 2021)
mouly.payment()