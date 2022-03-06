import unittest

from src.karaoke_venue import KaraokeVenue
from src.guest import Guest
from src.room import Room

class KaraokeVenueTest(unittest.TestCase):
    def setUp(self):
        self.like_a_dragon = KaraokeVenue("Like a Dragon", 2000)

    def test_check_venue_has_name(self):
        self.assertEqual("Like a Dragon", self.like_a_dragon.name)

    def test_check_lobby_is_empty_at_start(self):
        self.assertEqual([], self.like_a_dragon.lobby)

    def test_check_till_has_starting_balance(self):
        self.assertEqual(2000, self.like_a_dragon.till)

    def test_cash_can_be_added_to_balance(self):
        self.like_a_dragon.add_cash_to_till(500)

        self.assertEqual(2500, self.like_a_dragon.till)

    # def test_guests_can_move_from_lobby_into_a_room(self):

    # def test_guests_can_move_from_room_into_lobby(self):