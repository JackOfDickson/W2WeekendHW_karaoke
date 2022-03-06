import unittest
from src.guest import Guest

class GuestTest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Kazuma Kiryu", "Judgement", 2000)
    
    def test_guest_has_name(self):
        self.assertEqual("Kazuma Kiryu", self.guest1.name)
    
    def test_cheer_for_fav_song(self):
        cheer = self.guest1.cheer_for_fav_song_is_playing()

        self.assertEqual(cheer, "whoo! I love Judgement!")
    
    def test_guest_has_wallet(self):
        self.assertEqual(2000, self.guest1.wallet)
