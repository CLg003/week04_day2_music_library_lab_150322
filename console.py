from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository

artist_1 = Artist('Beyonce')

artist_repository.save(artist_1)
