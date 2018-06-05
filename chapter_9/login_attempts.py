class User:
    """Stores the attributes of users."""
    def __init__(self, first_name, last_name, age, middle_name = ' '):
        """Initializing user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.middle_name = middle_name
        self.login_attempts = 0

    def describe_user(self):
        """Describes the attributes of a user."""
        print("This is a description of the user: ")
        if self.middle_name:
            full_name = ("Full Name: " + self.first_name + " "
            + self.middle_name + " "
            + self.last_name + " age: " + str(self.age))
        else:
            full_name = ("Full Name: " + self.first_name + " "
            + self.last_name +
             " age: " + str(self.age))
        print(full_name.upper())

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print("Whats good? " + self.first_name.upper()
        + " " + self.last_name.upper())

    def increment_login_attempts(self, *login_attempts):
        """Adds increments of 1 to login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self, *login_attempts):
        """Resets login attempts to zero."""
        self.login_attempts = 0


chris = User("Christopher", "Leader", 30, "Nicholas")
matt = User("Matthew", "Demayo", 32)

chris.login_attempts = 0
print(chris.login_attempts)
chris.increment_login_attempts()
chris.increment_login_attempts()
chris.increment_login_attempts()
chris.increment_login_attempts()
chris.increment_login_attempts()

print(chris.login_attempts)

chris.reset_login_attempts()
print(chris.login_attempts)
