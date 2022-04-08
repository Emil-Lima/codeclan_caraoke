import unittest
from src.karaoke import Karaoke
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestKaraoke(unittest.TestCase):
    def setUp(self):
        room1 = Room("name of room 1", ["a first list of songs",  "here"], ["a first list of customers", "here"])
        room2 = Room("name of room 2", ["a second list of songs",  "here"], ["a second list of customers", "here"])
        self.list_of_rooms = [room1, room2]

        self.karaoke1 = Karaoke("name of karaoke 1", self.list_of_rooms)
    
    def test_karaoke_has_a_name(self):
        self.assertEqual("name of karaoke 1", self.karaoke1.name)

    def test_karaoke_has_list_of_rooms(self):
        self.assertEqual(self.list_of_rooms, self.karaoke1.rooms)

    def test_karaoke_can_add_new_room(self):
        room_new = Room("name of new room", ["list of songs"], ["list of customers"])
        self.karaoke1.add_room(room_new)
        self.assertEqual(room_new, self.karaoke1.rooms[-1])
        self.assertEqual(3, len(self.karaoke1.rooms))