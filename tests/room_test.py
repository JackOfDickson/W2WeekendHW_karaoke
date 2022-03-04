import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class RoomTest(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(1)
        self.guest1 = Guest("Kazuma Kiryu")
        self.guest2 = Guest("Goro Majima")
        self.song1 = Song("Judgement", 123, "rock")
        self.song2 = Song("Baka Mitai", 121, "pop")
    
    def test_room_has_number(self):
        self.assertEqual(1, self.room1.room_number)
    
    def test_room_has_empty_guest_list(self):
        self.assertEqual(0, len(self.room1.guests))
    
    def test_room_has_no_songs_playing(self):
        self.assertEqual(None, self.room1.current_song)
    
    def test_room_has_empty_song_queue(self):
        self.assertEqual(0, len(self.room1.song_queue))

#TESTING METHODS

    #Guest Related Tests

    def test_room_has_guest(self):
        self.room1.check_in_guest(self.guest1)

        self.assertEqual(1, len(self.room1.guests))
    
    def test_remove_guest_from_room(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_in_guest(self.guest2)
        duet_room = len(self.room1.guests)

        self.room1.check_out_guest(self.guest1)
        self.assertEqual(2, duet_room)
        self.assertEqual(1, len(self.room1.guests))
    
    #Song Related Tests
    
    def test_check_current_song_when_nothing_has_been_queued(self):
        check_song = self.room1.check_current_song()

        self.assertEqual(check_song, self.room1.current_song)
    
    def test_check_current_song_when_song_is_queued(self):
        self.room1.queue_song(self.song1)

        self.assertEqual(self.song1, self.room1.current_song)
    
    def test_queued_song_is_played_when_nothing_is_queued(self):
        self.room1.queue_song(self.song1)

        self.assertEqual(self.song1, self.room1.current_song)
    
    def test_song_is_put_on_queue_when_song_is_playing(self):
        self.room1.queue_song(self.song1)
        self.room1.queue_song(self.song2)

        self.assertEqual(1, len(self.room1.song_queue))
