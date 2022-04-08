import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("John", 50, "song I like")

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest1.name)

    def test_guest_has_money(self):
        self.assertEqual(50, self.guest1.money)

    def test_customer_has_favourite_song(self):
        self.assertEqual("song I like", self.guest1.favourite_song)