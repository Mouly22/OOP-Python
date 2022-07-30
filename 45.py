class Team:
    def __init__(self, country, win, language = 'Spanish'):
        self.country = country
        self.win = win
        self.language = language
        self.forcost = 0
        self.defcost = 0
        self.tcost = 0
        self.dct = {}
        self.player_list = 'No players assigned yet'
        self.fcount = 0
        self.dcount = 0

    
    def calculateCost(self):
        if len(self.dct.keys()) == 0:
            print('No cost yet as there is no players')
        else:
            self.tcost = self.forcost + self.defcost
            print(f'Total cost:{self.tcost}')   
            
    def printDetail(self):
        print(f'Team Name:{self.country}')
        print(f'World Cup Win:{self.win}')
        print(f'Language:{self.language}')
        for m, n in self.dct.items():
            if len(m) == 0:
                pass
            else:
                if m == 'Forward':
                    print(f'{m}s:')
                    for r, s in n.items():
                        print(r)
                elif m == 'Defender':
                    print(f'{m}s:')
                    for r, s in n.items():
                        print(r)               
       
        
    def addPlayer(self, players):
        self.player_list = []
        if players.position not in self.dct.keys():
            self.dct[players.position] = {players.name: (players.name, players.position)}
        else:
            if players.name not in self.dct[players.position].keys():
                self.dct[players.position][players.name] = (players.name, players.position)
                
        if players.position == 'Forward':
            self.fcount += 1
            self.forcost = self.fcount * 500
        elif players.position == 'Defender':
            self.dcount += 1
            self.defcost = self.dcount * 450
                
        for u, v in self.dct.items():
            for a, b in v.items():
                self.player_list.append(b)
                
            
class Player:
    def __init__(self, name, position = 'Forward'):
        self.name = name
        self.position = position

argentina = Team("Argentina", 2)
print("1.============================================")
print(argentina.player_list)
print("2.============================================")
argentina.calculateCost()
print("3.============================================")
argentina.printDetail()
print("4.============================================")
messi = Player("Messi")
maria = Player("Maria")
marcos = Player("Marcos", "Defender")
argentina.addPlayer(messi)
argentina.addPlayer(maria)
argentina.addPlayer(marcos)
print("5.============================================")
argentina.calculateCost()
print("6.============================================")
argentina.printDetail()
print("7.============================================")
print(argentina.player_list)
print("8.###############################################")
brazil = Team("Brazil", 5, "Portuguese")
print("9.============================================")
print(brazil.player_list)
print("10.============================================")
brazil.calculateCost()
print("11.============================================")
brazil.printDetail()
print("12.============================================")
silva = Player("Silva", "Defender")
neymar = Player("Neymar")
brazil.addPlayer(silva)
brazil.addPlayer(neymar)
print("13.============================================")
brazil.calculateCost()
print("14.============================================")
brazil.printDetail()
print("15.============================================")
print(brazil.player_list)