from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()


artist_1 = Artist('Beyonce')
artist_repository.save(artist_1)

artist_2 = Artist('Arlo Parks')
artist_repository.save(artist_2)

album_1 = Album('Lemonade', 'pop', artist_1)
album_repository.save(album_1)

album_2 = Album('Collapsed in Sunbeams', 'pop', artist_2)
album_repository.save(album_2)

artist_repository.select(artist_1.id)
album_repository.select(album_1.id)

artists = artist_repository.select_all()
for artist in artists:
    print(artist.__dict__)

albums = album_repository.select_all()
for album in albums:
    print(album.__dict__)