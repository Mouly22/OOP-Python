class Team:
    def __init__(self, tname= None):
        self.__tname = tname
        self.__plst = []
        
    def setName(self, tname):
        self.__tname = tname
        
    def addPlayer(self, other):
        self.__plst.append(other.pname)
        
    def printDetail(self):
        print('==========')
        print(f'Team: {self.__tname}')
        print('List of Players:')
        print(self.__plst)
        print('==========')

class Player:
    def __init__(self, pname):
        self.pname = pname

b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()