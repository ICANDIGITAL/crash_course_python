def show_magicians(magicians):
    """Displays the name of each magicians in a list."""
    for magician in magicians:
        print(magician.title())

magical = ['aalto simo', 'al baker', 'alessandro cagliostro', 'paul daniels']

def make_great(tricks):
    """Modifies the original function by adding a message."""
    for great in range(len(tricks)):
        tricks[great] += " the great".title()

make_great(magical[:])
show_magicians(magical)
