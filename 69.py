class Product:
    def __init__(self,id, title, price):
        self.__id = id
        self.__title = title
        self.__price = price
    def get_id_title_price(self):
        return "ID: "+str(self.__id)+" Title:" +self.__title + " Price: "+str(self.__price)
    
class Book(Product):
    def __init__(self, id, title, price, isbn, publisher):
        super().__init__(id, title, price)
        self.isbn = isbn
        self.publisher = publisher
    def printDetail(self):
        return(f'{super().get_id_title_price()} \nISBN: {self.isbn} \nPublisher: {self.publisher}')
class CD(Product):
    def __init__(self, id, title, price, band, duration, genre):
        super().__init__(id, title, price)
        self.band = band
        self.duration = duration
        self.genre = genre
    def printDetail(self):
        return(f'{super().get_id_title_price()} \nBand: {self.band} Duration: {self.duration} \nGenre: {self.genre}')

    
#write your code here
book = Book(1,"The Alchemist",500,"97806","HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2,"Shotto",300,"Warfaze",50,"Hard Rock")
print(cd.printDetail())