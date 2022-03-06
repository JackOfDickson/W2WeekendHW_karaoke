class KaraokeVenue:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.lobby = []
        self.rooms = []
    
    def add_cash_to_till(self, amount):
        self.till += amount
    
    def guest_enter_lobby(self, guest):
        self.lobby.append(guest)

    def guest_leave_lobby(self, guest):
        self.lobby.remove(guest)

    def open_up_room(self, room):
        self.rooms.append(room)


    def move_guest_from_lobby(self, room, guest):
        (room).check_in_guest(guest)
        self.guest_leave_lobby(guest)