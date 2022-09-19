class Tournament:
    def __init__(self,name='Default'):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    
class Cricket_Tournament(Tournament):
    def __init__(self, name = 'Default', no_of_teams =0, types= 'No type'):
        super().__init__(name = name)
        self.name = super().get_name()
        self.no_of_teams = no_of_teams
        self.types = types
    def detail(self):
        return(f'Ckicket Tournament Name: {self.name} \nNumber of Teams: {self.no_of_teams} \nType: {self.types}')

class Tennis_Tournament(Tournament):
    def __init__(self, name, no_of_teams):
        super().__init__(name = name)
        self.name = super().get_name()
        self.no_of_teams = no_of_teams
        
    def detail(self):
        return(f'Tennis Tournament Name: {self.name} \nNumber of Teams: {self.no_of_teams}')

ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())