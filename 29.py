class Match:
    def __init__(self, name):
        name = name.split('-')
        self.name = name
        self.run = 0
        self.wicket = 0
        print('5..4..3..2..1.. Play !!!')

    def add_run(self, run):
        self.run += run   

    def add_over(self, over):
        if over < 5:
            self.over = over
        else:
            
            print(f'Warning! Cannot add {over} over/s (5 over match)')   
       
    def add_wicket(self, wicket = 0):
        self.wicket = wicket
        
    def print_scoreboard(self):
        print(f'Batting Team: {self.name[0]}')
        print(f'Bowling Team: {self.name[1]}')
        return(f'Total Runs: {self.run} Wickets: {self.wicket} Overs: {self.over}')
        

match1 = Match("Rangpur Riders-Cumilla Victorians")
print("=========================")
match1.add_run(4)
match1.add_run(6)
match1.add_over(1)
print(match1.print_scoreboard())
print("=========================")
match1.add_over(5)
print("=========================")
match1.add_wicket(1)
print(match1.print_scoreboard())