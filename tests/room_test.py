import unittest
from src.room import Room

class RoomTest(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(1)
    
    def test_room_has_number(self):
        self.assertEqual(1, self.room1.room_number)
    
    def test_room_has_empty_guest_list(self):
        self.assertEqual(0, len(self.room1.guests))
    
    def test_room_has_no_songs_playing(self):
        self.assertEqual(None, self.room1.current_song)
