import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("name of song 1")

    def test_song_has_name(self):
        self.assertEqual("name of song 1", self.song1.name)