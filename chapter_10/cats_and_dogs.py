from silent_cats_and_dogs import File_Pass
filename = 'cats.txt'
filename_2 = 'dogs.txt'


class File_No_Pass(File_Pass):
    """A class that read the contents of any file."""
    def __init__(self, filename):
        """Initializing mother function attributes."""
        super().__init__(filename)

    def read_lines_no_pass(self):
        """Read the lines of cats.txt & dogs.txt with a silent fail."""
        try:
            with open(self.filename) as file_object:
                contents = file_object.readlines()
                for content in contents:
                    print(content.title())
        except FileNotFoundError:
            print("This file cannot be located. Please try again.")


text = File_No_Pass(filename)
text.read_lines_no_pass()
print("\n")
text_2 = File_No_Pass(filename_2)
text_2.read_lines_no_pass()
