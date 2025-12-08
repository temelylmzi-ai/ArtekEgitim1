class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("Movie objesi olusturuldu")
        
    def __str__(self):
        return self.title

    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("Movie silindi")

m1 = Movie("a","b",124)

print(len(m1))