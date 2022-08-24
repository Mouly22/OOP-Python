class Random:
    def __init__(self, name, rn):
        self.name = name
        self.rn = rn

c1 = Random('mouly', 5)
c2 = Random('fahad', 2)
print(c2)       
#amra jokhon print(c2) print dicchi tokhon amader memory location er jekhane ei object ta ache seikhaner address ta print hbe. 
#Eta basically (c2.__str__()) er maddhome ekta string back kore. 
#amra method overriding er maddhome ei c2 print dile jei likha asbe seita k override korte pari.
class Random:
    def __init__(self, name, rn):
        self.name = name
        self.rn = rn

    def __str__(self):
        return (f"This is {self.name}'s object")
c1 = Random('mouly', 5)
c2 = Random('fahad', 2)
print(c2)

#output: This is fahad's object