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

        self.room1 = Room("room1", self.list_of_songs, self.list_customers, 50)

        self.room2 = Room("room2", self.list_customers, self.list_of_songs, 2)

    def test_room_has_a_name(self):
        self.assertEqual("room1", self.room1.name)
    
    def test_room_has_list_of_songs(self):
        self.assertEqual(self.list_of_songs, self.room1.songs)

    def test_room_has_list_of_customers(self):
        self.assertEqual(self.list_customers, self.room1.customers)

    def test_room_has_maximum_capacity(self):
        self.assertEqual(50, self.room1.maximum_capacity)

    def test_room_can_add_one_new_guest(self):
        guest_new = Guest("Jane", 500)
        self.room1.add_guest(guest_new)
        self.assertEqual(guest_new, self.room1.customers[-1])

    def test_room_can_check_out_a_guest(self):
        customer_to_check_out = self.room1.customers[0]
        customer_that_stays = self.room1.customers[1]
        self.room1.check_out_guest(customer_to_check_out)
        self.assertEqual(1, len(self.room1.customers))
        self.assertEqual(customer_that_stays, self.room1.customers[0])

    def test_room_can_add_one_new_song(self):
        song_new = Song("name of new song", "techno")
        self.room1.add_song(song_new)
        self.assertEqual(song_new, self.room1.songs[-1])

    def test_room_does_not_exceed_max_capacity(self):
        guest_new = Guest("Jane", 500)
        self.room2.add_guest(guest_new)
        self.assertEqual(2, len(self.room2.customers))

