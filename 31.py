class Batsman:
    def __init__(self, *vals):
        if type(vals[0]) == str:
            self.name = vals[0]
            self.run = vals[1]
            self.ball = vals[2]
        else:
            self.name = "New Batsman"
            self.run = vals[0]
            self.ball = vals[1]
           
        
    def printCareerStatistics(self):
        
        print(f'Name: {self.name}')
        print(f'Runs Scored: {self.run}, Balls Faced: {self.ball}')
        
    def battingStrikeRate(self):
        self.score = (self.run / self.ball) * 100
        return self.score
        
    def setName(self, name):
        self.name = name
        
        
    
b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())