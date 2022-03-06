from shutil import move
import unittest

from src.karaoke_venue import KaraokeVenue
from src.guest import Guest
from src.room import Room

class KaraokeVenueTest(unittest.TestCase):
    def setUp(self):
        self.like_a_dragon = KaraokeVenue("Like a Dragon", 2000)
        self.room1 = Room(1, 2, 100)
        self.guest1 = Guest("Kazuma Kiryu", "Judgement", 2005)
        self.guest2 = Guest("Goro Majima", "Get to the Top!", 565656565)
        self.guest3 = Guest("Ichiban kasuga", "The Future I Dreamed of", 1)

    def test_check_venue_has_name(self):
        self.assertEqual("Like a Dragon", self.like_a_dragon.name)

    def test_check_lobby_is_empty_at_start(self):
        self.assertEqual([], self.like_a_dragon.lobby)

    def test_check_till_has_starting_balance(self):
        self.assertEqual(2000, self.like_a_dragon.till)

    def test_cash_can_be_added_to_balance(self):
        self.like_a_dragon.add_cash_to_till(500)

        self.assertEqual(2500, self.like_a_dragon.till)

    def test_guest_enters_lobby(self):
        self.like_a_dragon.guest_enter_lobby(self.guest1)
        self.assertEqual([self.guest1], self.like_a_dragon.lobby)

    def tests_open_up_room(self):
        self.like_a_dragon.open_up_room(self.room1)
        self.assertEqual([self.room1], self.like_a_dragon.rooms)


    def test_guests_can_move_from_lobby_into_a_room(self):
        self.like_a_dragon.open_up_room(self.room1)
        self.like_a_dragon.guest_enter_lobby(self.guest1)
        self.like_a_dragon.move_guest_from_lobby(self.room1, self.guest1)

        self.assertEqual([self.guest1], self.room1.guests)
        self.assertEqual(self.room1, self.like_a_dragon.rooms[0])

    # def test_guests_can_move_from_room_into_lobby(self):