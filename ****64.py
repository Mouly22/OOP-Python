class SultansDine:
    t_brnch = 0
    t_sell = 0
    brnch_lst = []
    
    @staticmethod
    def details():
        print(f'Total Number of branch(s): {SultansDine.t_brnch} \nTotal Sell: {SultansDine.t_sell} Taka')
        for i in SultansDine.brnch_lst:
            print(f'Branch Name: {i[0]}, Branch Sell: {i[1]}')
            print(f'Branch consists of total sell\'s:{round(((i[1]/ SultansDine.t_sell) * 100),2)}%')
            
            
    def __init__(self, bname):
        self.bname = bname
        SultansDine.t_brnch += 1
        self.bsell =0
        self.per = 0
        
    def sellQuantity(self, s_qul):
        if s_qul < 10:
            self.bsell = s_qul * 300
            
        elif s_qul < 20:
            self.bsell = s_qul * 350
            
        else:
            self.bsell = s_qul * 400
            
        SultansDine.t_sell += self.bsell
        SultansDine.brnch_lst.append([self.bname, self.bsell])
            
            
            
    def branchInformation(self):
        print(f'Branch Name: {self.bname} \nBranch Sell: {self.bsell}')
            
    


SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()   