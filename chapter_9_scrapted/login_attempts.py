class User():
    """A simple attempt to model a user profile."""
    def __init__(self, first_name, last_name, age, race, home_town):
        """Initialize user profile attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.race = race
        self.home_town = home_town
        self.login_attempts = 0

    def describe_user(self):
        """Displays a discription of a user's profile."""
        print("This is the current user's information:" + "\n" +
        self.first_name.title() + "\n" + self.last_name.title() + "\n" +
        str(self.age) + "\n" + self.race.upper() + "\n" +
        self.home_town)

    def greet_user(self):
        """Displays a basic greeting for a user."""
        full_name = self.first_name + " " + self.last_name
        print("Hello, " + full_name + "!")

    def login_attempts(self):
        """Adds incremental value of one to login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value of login attempts."""
        self.login_attempts <= 0

chris = User("Shitty", "Butt Bill", "30", "Dark Chocolate", "DMV")
john = User("Burt", "McGurt", "28", "Milk Chocolate", "The Country")

chris.describe_user()
chris.greet_user()
print("\n")
john.describe_user()
john.greet_user()

print("\n")
incremental_login_attempts = User("Rib", "Tickeler", "18", "Ebony", "Hood")
