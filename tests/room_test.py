import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        guest1 = Guest("Emilio", 100)
        guest2 = Guest("John", 200)
        song1 = Song("name of song 1", "rock")
        song2 = Song("name of song 2", "pop")
        self.list_of_songs = [song1, song2]
        # self.room1 = Room("room1", ["song1", "song2", "song3"], [guest_1, guest_2])
        self.room1 = Room("room1", self.list_of_songs)

    def test_room_has_a_name(self):
        self.assertEqual("room1", self.room1.name)
    
    def test_room_has_list_of_songs(self):
        self.assertEqual(self.list_of_songs, self.room1.songs)