class Panda:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        
    def sleep(self, time = 0):
        self.time = time
        if self.time > 3 and self.time < 5:
            itm = 'Mixed Veggies'
        elif self.time > 6 and self.time < 8:
            itm = 'Eggplant & Tofu'
        elif self.time > 9 and self.time < 11:
            itm = 'Broccoli Chicken'
        else:
            itm = 'bamboo leaves'
            return(f"{self.name}'s duration is unknown thus should have only {itm}")
            
        return(f'{self.name} sleeps {self.time} hours daily and should have {itm}')     
        
panda1 = Panda("Kunfu","Male", 5)
panda2=Panda("Pan Pan","Female",3)
panda3=Panda("Ming Ming","Female",8)
print("{} is a {} Panda Bear who is {} years old".format(panda1.name,panda1.gender,panda1.age))
print("{} is a {} Panda Bear who is {} years old".format(panda2.name,panda2.gender,panda2.age))
print("{} is a {} Panda Bear who is {} years old".format(panda3.name,panda3.gender,panda3.age))
print("===========================")
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())