class Guest:
    def __init__(self, name, fav_song):
        self.name = name
        self.fav_song = fav_song

    def cheer_for_fav_song_is_playing(self):
        return f"whoo! I love {self.fav_song}!"