class Hotel:
    def __init__(self, hname):
        self.hname = hname
        self.gid = None
        self.slst = []
        self.gnlst = []
        self.gilst = []
        self.galst =[]
        self.gplst =[]
    def addStuff(self, sname, sage, sid = 0, sphno = '000'):
        self.sname = sname
        self.sage = sage 
        self.sid = sid
        self.sphno = sphno
        self.sid += 1
        self.slst.append(self.sname)
        print(f'Staff with ID {self.sid} is added')
        
    def getStuffById(self, sid):
        self.sid = sid
        print(f'Staff ID: {self.sid}')
        print(f'Name: {self.sname}')
        print(f'Age: {self.sage}')
        return(f'Phone no.: {self.sphno}')
            
        
    def addGuest(self, gname, gage, gphno, gid = 1):
        self.gname = gname
        self.gage = gage 
        self.gphno = gphno
        self.gnlst.append(self.gname)
        self.galst.append(self.gage)
        self.gplst.append(self.gphno)
        
        if self.gid != None:
            self.gid += 1
        else:
            self.gid = gid
        self.gilst.append(self.gid)
        print(f'Guest with ID {self.gid} is created')
        
    def getGuestById(self, gid):
        self.gid = gid
        print(f'Guest ID: {self.gid}')
        print(f'Name: {self.gname}')
        print(f'Age: {self.gage}')
        return(f'Phone no.: {self.gphno}')
        
    def allStaffs(self):
        print(f'Number of Staff: {len(self.slst)}')
        print(f'Staff ID: {self.sid} Name: {self.sname} Age: {self.sage} Phone no: {self.sphno}')
        
    def allGuest(self):
        print(f'Number of Guest: {len(self.gnlst)}')
        for i in range(len(self.gnlst)):
            print(f'Guest ID: {self.gilst[i]} Name: {self.gnlst[i]} Age: {self.galst[i]} Phone no: {self.gplst[i]}')
        
        
        
            
        
h = Hotel("Lakeshore")
h.addStuff( "Adam", 26)
print("=================================")
print(h.getStuffById(1))
print("=================================")
h.addGuest('Carol',35,'123')
print("=================================")
print(h.getGuestById(1))
print("=================================")
h.addGuest("Diana", 32, '431')
print("=================================")
print(h.getGuestById(2))
print("=================================")
h.allStaffs()
print("=================================")
h.allGuest()