class Spotify:
    def __init__(self,k):
        self.plst = list(k)
        print("Welcome to Spotify!")
    def playing_number(self,num):
        if num > len(self.plst):
            return(f"{num} number song not found. Your playlist has {len(self.plst)} songs only.")
        else:
            print("##########################")
            print(f"Playing {num} number song for you")
            return f"Song name: {self.plst[num - 1]}"
    def add_to_playlist(self,sname):
        self.plst.append(sname)

user1 = Spotify(["See You Again", "Uptown Funk", "Hello"])
print("=========================")
print(user1.playing_number(4))
user1.add_to_playlist("Dusk Till Dawn")
print(user1.playing_number(3))
print(user1.playing_number(4))