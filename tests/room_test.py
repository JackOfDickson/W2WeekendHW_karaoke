import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class RoomTest(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(1)
        self.guest1 = Guest("Kazuma Kiryu")
        self.guest2 = Guest("Goro Majima")
        self.song1 = Song("Judgement", 227, "rock")
    
    def test_room_has_number(self):
        self.assertEqual(1, self.room1.room_number)
    
    def test_room_has_empty_guest_list(self):
        self.assertEqual(0, len(self.room1.guests))
    
    def test_room_has_no_songs_playing(self):
        self.assertEqual(None, self.room1.current_song)
    
    def test_room_has_empty_song_queue(self):
        self.assertEqual(0, len(self.room1.song_queue))

#TESTING METHODS

    def test_room_has_guest(self):
        self.room1.add_guest(self.guest1)

        self.assertEqual(1, len(self.room1.guests))
    
    def test_check_current_song_when_nothing_has_been_queued(self):
        check_song = self.room1.check_current_song()

        self.assertEqual(check_song, self.room1.current_song)
    
    # def test_check_current_song_when_song_is_queued(self):
        
