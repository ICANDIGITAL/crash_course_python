def make_album(artist,title,tracks=''):
    """Creates a dictionary of albums."""
    album = {"By":artist,"Titled":title, "Tracks": tracks}
    return album

while True:
    print("\nPlease provide the exact details of your favorite album.")
    print("Enter q any time to quit.")
    artist=input("What is this artist's name?")
    if artist == 'q':
        break
    title=input("\nNext, input the title of the album:")
    if title == 'q':
        break
    tracks=input("\nFinally, input the number of tracks:")
    if tracks == 'q':
        break
