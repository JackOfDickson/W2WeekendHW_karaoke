import unittest
from src.guest import Guest

class GuestTest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Kazuma Kiryu")
    
    def test_guest_has_name(self):
        self.assertEqual("Kazuma Kiryu", self.guest1.name)
