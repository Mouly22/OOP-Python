class PokemonTrainer:
  def __init__(self, name, a, b, c = ''):
    self.name = name
    self.a = a
    self.b = b
    self.c = c

  def info(self):
    print(f"Trainer name: {self.name}")
    if self.c == '':
      print(f'Pokemons caught: {self.a} || {self.b} || {self.c}')
    else:
      print(f'Pokemons caught: {self.a} || {self.b} || {self.c} ||')

  def catch(self, pok):
    print('Caught successfully')
    self.pok = pok
    self.c = pok
    

c1 = PokemonTrainer('ash ketchum','pikachu', 'bulbasaur')
print('---')
c1.info()
print('---')

c2 = PokemonTrainer('Brock','Onix', 'Zubat', 'Mudkip')
c2.info()
print('---')
c1.catch('Snorlax')
c1.info()