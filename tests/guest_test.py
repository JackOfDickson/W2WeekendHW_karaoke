from concurrent.futures.process import _chain_from_iterable_of_lists
import unittest
from src.guest import Guest

class GuestTest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Kazuma Kiryu", "Judgement")
    
    def test_guest_has_name(self):
        self.assertEqual("Kazuma Kiryu", self.guest1.name)
    
    def test_cheer_for_fav_song(self):
        cheer = self.guest1.cheer_for_fav_song_is_playing()

        self.assertEqual(cheer, "whoo! I love Judgement!")
