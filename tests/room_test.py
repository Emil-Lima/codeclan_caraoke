import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        guest_1 = Guest("Emilio", 100)
        guest_2 = Guest("John", 200)
        self.room1 = Room("room1", ["song1", "song2", "song3"], [guest_1, guest_2])

    def test_room_has_a_name(self):
        self.assertEqual("room1", self.room1.name)
    