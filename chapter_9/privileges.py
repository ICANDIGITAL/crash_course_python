class Privilges():
    """Stores a list of privileges unique to admin users."""
    def __init__(self, *privileges):
        """Initialize attributes of class."""
        self.privileges = privileges

    def show_privileges(self):
        """Print a statement listing privileges common to Admin users."""
        print("\n")
        print("This user has the following privileges:")
        print("-can add post \n-can delete post \n-can ban user")
