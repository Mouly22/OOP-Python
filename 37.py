class Group:
    def __init__(self, team, wrd):
        self.team = team
        self.wrd = wrd
        print(f'{self.team} just got formed!')
        self.lst = []
    
    def add_member(self, *mbr):
        if len(self.lst) < 5:
            for i in mbr:
                self.lst.append(i)
        else:
            print("No more passengers can be added!")
        
       
    def show_member(self):
        val = ''
        for p in self.lst:
            val += p +', '
        val = val.rstrip(', ')   
        print(val)
        
    def remove_member(self, name):
        self.name = name
        if self.name in self.lst:
            self.lst.remove(self.name)

group1 = Group('A001', 'A')
print('-------------------------------')
group1.add_member("Steven_Wilson", "Gavin_Harrison")
group1.show_member()
print('-------------------------------')
group1.add_member("Richard_Barbieri")
group1.show_member()
print('-------------------------------')
group2 = Group('B002', 'B')
print('-------------------------------')
group2.add_member("John_Petrucci", "John_Myung", "Jordan_Rudess",  "Mike_Portnoy", "James_LaBrie")
group2.show_member()
print('-------------------------------')
group2.add_member("Kevin_Moore")
print('-------------------------------')
group2.show_member()
print('-------------------------------')
group2.remove_member("Mike_Portnoy")
group2.show_member()
print('-------------------------------')
group2.add_member("Mike_Mangini")
group2.show_member()