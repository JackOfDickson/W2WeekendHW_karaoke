class KaraokeVenue:
    def __init__(self, name, till) -> None:
        self.name = name
        self.till = till
        self.lobby = []
        self.rooms = []
    
    def add_cash_to_till(self, amount):
        self.till += amount