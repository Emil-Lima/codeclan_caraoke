import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        guest1 = Guest("Emilio", 100)
        guest2 = Guest("John", 200)
        self.list_customers = [guest1, guest2]

        song1 = Song("name of song 1", "rock")
        song2 = Song("name of song 2", "pop")
        self.list_of_songs = [song1, song2]

        self.room1 = Room("room1", self.list_of_songs, self.list_customers)

    def test_room_has_a_name(self):
        self.assertEqual("room1", self.room1.name)
    
    def test_room_has_list_of_songs(self):
        self.assertEqual(self.list_of_songs, self.room1.songs)

    def test_room_has_list_of_customers(self):
        self.assertEqual(self.list_customers, self.room1.customers)

    def test_room_can_add_one_new_guest(self):
        guest_new = Guest("Jane", 500)
        self.room1.add_guest(guest_new)
        self.assertEqual(guest_new, self.room1.customers[-1])
