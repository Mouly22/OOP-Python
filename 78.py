class PokemonBasic:
    def __init__(self, name = 'Default', hp = 0, weakness = 'None', type = 'Unknown'):
        self.name = name
        self.hit_point = hp
        self.weakness = weakness
        self.type = type
        
        
    def get_type(self):
        return 'Main type: ' + self.type
    def get_move(self):
        return 'Basic move: ' + 'Quick Attack'
    def __str__(self):
        return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness

class PokemonExtra(PokemonBasic):
    def __init__(self, name = 'Default', hp = 0, weakness = 'None', *args):
        self.lst = []
        super().__init__(name = name, hp = hp, weakness = weakness)
        for x in args:
            self.lst.append(x)
  
       
    def __str__(self):
        return f'Name: {self.name}, HP: {self.hit_point}, Weakness: {self.weakness}'
    
    def get_type(self):
        if len(self.lst) == 1:
            self.type = self.lst[0]
            return f'Main type: {self.type}'
        else:
            self.type = self.lst[0]
            return f'Main type: {self.type}, Secondary type: {self.lst[1]}'
                
    def get_move(self):
        val = ''
        if len(self.lst) == 1:
            return super().get_move()
        else:
            
            for x in self.lst:
                g = self.lst[-1]
            for xx in g:
                val += xx + ', '
            val = val.rstrip(', ')
            return f'{super().get_move()} \nOther move: {val}'
    
        
        
    
print('\n------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())
print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water','Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())

print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water','Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())