class Room:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capactiy = capacity
        self.guests = []
        self.current_song = None
        self.song_queue = []
    
    def check_in_guest(self, guest):
        self.guests.append(guest)
    
    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def check_current_song(self):
        return self.current_song

    def queue_song(self, song):
        self.song_queue.append(song)
        if self.current_song == None:
            self.current_song = self.song_queue.pop(0)
    

