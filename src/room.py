class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.guests = []
        self.current_song = None
        self.song_queue = []
    
    def add_guest(self, guest):
        self.guests.append(guest)
    
    def remove_guest(self, guest):
        self.guests.remove(guest)

    def check_current_song(self):
        return self.current_song

    # def queue_song(self, song):
    

