class FilmBase:
    def __init__(self, tittle, dated, genre):
        self.tittle = tittle
        self.dated = dated
        self.genre = genre
        #variable
        self.playback = 0
        self._hiddenplayback = 0
    #def __repr__(self):
    #    return f"FilmBase(tittle={self.tittle}, dated = {self.dated}, genre = {self.genre})"
    def __str__(self):
       return f'{self.tittle} {self.dated} {self.genre}'
    #Filmy i seriale mają metodę play, która zwiększa liczbę odtworzeń danego tytułu o 1.
    def __recordup__(self, play=1):
        self.playback += play
    @property
    def hiddenplayback(self):
        return self._hiddenplayback
    @hiddenplayback.setter
    def hiddenplayback(self, playy = 1):
        _hiddenplayback += playy

class Series(FilmBase):
    def __init__(self, series_no, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.series_no = series_no
        self.season = season
        self.playback = 0
    def __repr__(self):
        return f"FilmBase(tittle={self.tittle}, dated = {self.dated}, genre = {self.genre}, series_no = {self.series_no}, season = {self.season})"

filmpos1 = FilmBase(tittle="Krzyk", dated="2015", genre="horror")
series1 =Series(tittle="You", dated ="2022", genre="romance",series_no="01", season="01")
#Przechowuje filmy i seriale w jednej liście.
BaseList=list([])
BaseList=[filmpos1, series1]
print(BaseList)
#Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”.
print(filmpos1)
print(filmpos1.tittle)
print(series1)
print(series1.season)
#czy dwa dodatkowe parametry powinny być w klasie FilmBase aby wyświelała je klasa Series ?
result1 = filmpos1.playback
result2 = filmpos1.hiddenplayback
print(result1)
print(result2)
#filmpos1.hiddenplayback(40)
#print(result2)
