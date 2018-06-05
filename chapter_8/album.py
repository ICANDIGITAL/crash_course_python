def make_album(artist,title,tracks=''):
    """Creates a dictionary of albums."""
    album = {"By":artist,"Titled":title, "Tracks": tracks}
    return album

album_1 = make_album('DMX', "It's Dark and Hell is Hot","19")
print(album_1)

album_2 = make_album("Ghostface Killah", "Supreme Clientele")
print(album_2)

album_3 = make_album("Big L", "The Big Picture")
print(album_3)
