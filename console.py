from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()


artist_1 = Artist('Beyonce')
artist_repository.save(artist_1)

album_1 = Album('Lemonade', 'pop', artist_1)
album_repository.save(album_1)
