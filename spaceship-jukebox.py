class Song:
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
    