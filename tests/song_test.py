import unittest
from src.song import Song

class SongTest(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Judgement", 227, "rock")
    
    def test_song_has_name(self):
        self.assertEqual("Judgement", self.song1.title)

    def test_song_has_duration(self):
        self.assertEqual(227, self.song1.duration)

    def test_song_has_genre(self):
        self.assertEqual("rock", self.song1.genre)