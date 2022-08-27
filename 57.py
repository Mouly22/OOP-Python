
class Assassin:
    assa_no = 0
    def __init__(self, name, s_rate):
        self.name = name
        self.s_rate = s_rate
        Assassin.assa_no += 1

    def printDetails(self):
        print(f'Name:{self.name} \nSuccess rate: {self.s_rate}% \nTotal number of Assassin: {Assassin.assa_no}')

    @classmethod
    def failureRate(cls, name, f_rate):
        obj = cls(name, 100 - f_rate)
        return obj

    @classmethod
    def failurePercentage(cls, name, f_per):
        f_per = f_per[0:-1]
        f_per = float(f_per)
        obj = cls(name, 100 - f_per)
        return obj

john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()