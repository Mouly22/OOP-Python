class Team:
    def __init__(self, cname):
        self.cname = cname
        self.dct = {}
        
    def addPlayer(self, *args):
        for itms in args:
            if itms.role != None:
                print(f'{itms.name} added in team.')
            else:
                print('A player cannot be added without a role.') 
                
            if itms.role not in self.dct.keys():
                self.dct[itms.role] = {itms.name: [itms.age]}
            else:
                if itms.name not in self.dct[itms.role].keys():
                    self.dct[itms.role][itms.name] = [itms.age]
                       
    def showPlayers(self):
        for i, j in self.dct.items():
            if i == 'Batsman':
                print(f'{i}:')
                for m, n in j.items():
                    for r in n:
                        print(f'Player name: {m} Jersey No: {r}')
            if i == 'Bowler':
                print(f'{i}:')
                for m, n in j.items():
                    for r in n:
                        print(f'Player name: {m} Jersey No: {r}')   
                       
    
class Player:
    def __init__(self, *players):
        if len(players) == 2:
            self.name = players[0]
            self.age = players[1]
            self.role = None
        elif len(players) == 3:
            self.name = players[0]
            self.role = players[1]
            self.age = players[2]
        
    def setRole(self, role):
        self.role = role



team = Team("Bangladesh")
p1 = Player("Mahmudullah", "Batsman",30)
print("=================================")
team.addPlayer(p1)
print("=================================")
team.showPlayers()
print("=================================")
p2 = Player("Mustafizur Rahman", "Bowler",90)
p3 = Player("Tamim Iqbal", 28)
print("=================================")
team.addPlayer(p2,p3)
print("=================================")
team.showPlayers()
print("=================================")
p3.setRole("Batsman")
print("=================================")
team.addPlayer(p3)
print("=================================")
team.showPlayers()
print("=================================")
p4 = Player("Mushfiqur Rahim", "Batsman",15)
p5 = Player("Taskin Ahmed", "Bowler",3)
print("=================================")
team.addPlayer(p4,p5)
print("=================================")
team.showPlayers()