import unittest
from src.guest import Guest

class GuestTest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Kiryu Kazuma")
    
    def test_guest_has_name(self):
        self.assertEqual("Kiryu Kazuma", self.guest1.name)
