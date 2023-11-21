class Song():
    def __init__(self, title=None, artist=None):
        if title == None:
            self._title = "no title"
        else:
            self._title = title
        if artist == None:
            self._artist = "no artist"
        else:
            self._artist = artist
    
    def getTitle(self):
        return self._title
    def getArtist(self):
        return self._artist
    
    def play(self):
        return "Song is played"
    
class Album():
    def __init__(self, titles = None, songs = None):
        if titles == None:
            self._titles = [""]
        else:
            self._titles = titles
        if songs == None:
            self._songs = []
        else:
            self._songs = songs
    
    def getTitles(self):
        return self._titles
    def getSong(self, title):
        return self._songs(title)
    
class Library():
    def __init__(self, titles = None, albums = None):
        if titles == None:
            self._titles = [""]
        else:
            self._titles = titles
        if albums == None:
            self._albums = []
        else:
            self._albums = albums
    
    def getTitles(self):
        return self._titles
    def getSong(self, title):
        return self._albums(title)