class Ninja:
    def __init__(self):
        self.rank = 0
        self.stamina = 0.0

naruto = Ninja()
yellow_flash = Ninja()
naruto.rank = 1
naruto.stamina = 95.0
print(naruto.rank)
print(naruto.stamina)
yellow_flash.stamina = naruto.stamina - 2
print(yellow_flash.stamina)
yellow_flash.rank += (naruto.rank + 1)
print(yellow_flash.rank)
minato = yellow_flash
print(minato.rank)
print(minato.stamina)
naruto.rank = minato.rank - 1
naruto.stamina = yellow_flash.stamina + 3
print(naruto.rank)
print(naruto.stamina)
naruto.rank = -(-naruto.rank)
yellow_flash.stamina = -(-minato.stamina)
print(naruto.rank)
print(minato.stamina)