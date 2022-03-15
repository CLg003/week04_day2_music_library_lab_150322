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

album_3 = Album('Another Album', 'pop', artist_1)
album_repository.save(album_3)

artist_repository.select(artist_1.id)
album_repository.select(album_1.id)

albums = artist_repository.albums(artist_1)
# for album in albums:
#     print(album.__dict__)

# artist_1.name = 'Adele'
# artist_repository.update(artist_1)
# print(artist_1.__dict__)

# album_3.genre = 'heavy metal'
# album_repository.update(album_3)
# print(album_3.__dict__)

album_repository.delete_album(album_2.id)
artist_repository.delete_artist(artist_2.id)

artists = artist_repository.select_all()
for artist in artists:
    print(artist.__dict__)

albums = album_repository.select_all()
for album in albums:
    print(album.__dict__)
