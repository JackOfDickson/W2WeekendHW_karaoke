class Room:
    def __init__(self, room_number, capacity, entry_fee):
        self.room_number = room_number
        self.capactiy = capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.current_song = None
        self.song_queue = []
    
    def check_in_guest(self, guest):
        if len(self.guests) < self.capactiy:
            self.guests.append(guest)
        else:
            return f"room{self.room_number} is full, it has a capacity of {self.capactiy} people"

    
    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def check_current_song(self):
        return self.current_song

    def queue_song(self, song):
        self.song_queue.append(song)
        if self.current_song == None:
            self.current_song = self.song_queue.pop(0)
    

