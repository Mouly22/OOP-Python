class Football:
    def __init__(self, team_name, name, role):
        self.__team = team_name
        self.__name = name
        self.role = role
        self.earning_per_match = 0
    def get_name_team(self):
        return 'Name: '+self.__name+', Team Name: ' +self.__team
    
class Player(Football):
    def __init__(self, team_name, name, role, t_goal, t_played):
        super().__init__(team_name, name, role)
        self.t_goal = t_goal
        self.t_played = t_played
        self.ratio = 0
        self.match_earning = (self.t_goal * 1000) + (self.t_played * 10)
        
    def calculate_ratio(self):
        self.ratio = self.t_goal/self.t_played
        
    def print_details(self):
        print(f'{super().get_name_team()} \nTeam Role: {self.role} \nTotal Goal: {self.t_goal}, Total Played: {self.t_played} \nGoal Ratio: {self.ratio} \nMatch Earning: {self.match_earning}K')
        
class Manager(Football):
    def __init__(self, team_name, name, role, t_win):
        super().__init__(team_name, name, role)
        self.t_win = t_win
        self.match_earning = (self.t_win * 1000)
        
    def print_details(self):
        print(f'{super().get_name_team()} \nTeam Role: {self.role} \nTotal Win: {self.t_win} \nMatch Earning: {self.match_earning}K')
        
        
    
#write your code here
player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()