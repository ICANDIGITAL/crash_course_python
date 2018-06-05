from users import User


class Privileges:
    """Stores a list of privileges unique to admin users."""
    def __init__(self, *privileges):
        """Initialize attributes of class."""
        self.privileges = privileges

    def show_privileges(self):
        """Print a statement listing privileges common to Admin users."""
        print("\n")
        print("This user has the following privileges:")
        print("-can add post \n-can delete post \n-can ban user")


class Admin(User):
    """Create attributes specific to Admin users."""
    def __init__(self, first_name, last_name, age, middle_name=' '):
        """ Initialize attributes from parents class."""
        super().__init__(first_name, last_name, age, middle_name=' ')
        self.privileges = Privileges()


chris = Admin("Christopher", "Leader", 30, "Nicholas")
chris.describe_user()
chris.privilges.show_privilges()
