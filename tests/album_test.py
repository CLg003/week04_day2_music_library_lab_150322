import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    
    def setUp(self):
        self.album = Album('Greatest Hits', 'rock', 'Led Zeppelin')

    def test_album_has_title(self):
        self.assertEqual('Greatest Hits', self.album.title)

    def test_album_has_genre(self):
        self.assertEqual('rock', self.album.genre)

    def test_album_has_artist(self):
        self.assertEqual('Led Zeppelin', self.album.artist)
