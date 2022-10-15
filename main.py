import lyricsgenius

songname = input("Şarkı adını girin: ")
artistname = input("Sanatçı adı girin: ")

genius = lyricsgenius.Genius("GENİUS API KEY")

artist = genius.search_artist(artistname, max_songs=3, sort="title", include_features=True)
song = genius.search_song(songname, artist.name)
print(song.lyrics)
