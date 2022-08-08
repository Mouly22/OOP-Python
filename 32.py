class EPL_Team:
    def __init__(self, name, song = 'No Slogan', title_no = 0):
        self.name = name
        self.song = song
        self.title_no = title_no
        
    def showClubInfo(self):
        print(f'Name: {self.name}')
        print(f'Song: {self.song}')
        return(f'Total No of title: {self.title_no}')
        
    def increaseTitle(self):
        self.title_no += 1
        
    def changeSong(self, song):
        self.song = song
        
        
manu = EPL_Team('Manchester United', 'Glory Glory Man United')
chelsea = EPL_Team('Chelsea')
print('===================')
print(manu.showClubInfo())
print('##################')
manu.increaseTitle()
print(manu.showClubInfo())
print('===================')
print(chelsea.showClubInfo())
chelsea.changeSong('Keep the blue flag flying high')
print(chelsea.showClubInfo())