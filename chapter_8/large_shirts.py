def make_shirt(text='i love python', size='large'):
    """Displays the size and text printed on the shirt."""
    print("The selected shirt is a size " + size.lower() + " with a text of: "
    + text.title() + ".")

make_shirt()
make_shirt('i love python','medium')
make_shirt('top of the world ma', 'grande')
