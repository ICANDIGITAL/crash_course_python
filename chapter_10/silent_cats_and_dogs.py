class File_Pass:
    """A class that read the contents of any file."""
    def __init__(self, filename):
        """Initializing attributes."""
        self.filename = filename

    def read_lines(self):
        """Read the lines of cats.txt & dogs.txt with a silent fail."""
        try:
            with open(self.filename) as file_object:
                contents = file_object.readlines()
                for content in contents:
                    print(content.title())
        except FileNotFoundError:
            pass


text = File_Pass('dogs.txt')
text.read_lines()
print('\n')
text_2 = File_Pass('cats.txt')
text_2.read_lines()
