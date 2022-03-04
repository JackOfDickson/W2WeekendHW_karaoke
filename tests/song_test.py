from unicodedata import name
import unittest
from src.song import Song

class SongTest(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Judgement", 227, "rock")
    
    def song_has_name(self):
        self.assertEqual("Judgement", self.song1(name))

    # def song_has_duration(self):

    # def song_has_genre(self):