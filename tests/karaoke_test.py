import unittest
from src.karaoke import Karaoke
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestKaraoke(unittest.TestCase):
    def setUp(self):
        self.karaoke1 = ("name of karaoke 1")
    
    def test_karaoke_has_a_name(self):
        self.assertEqual("name of karaoke 1", self.karaoke1.name)