class Restaurant():
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisinse attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Dsiplays a discription of the restaurant."""
        print("The " + self.restaurant_name.title() + " serves a "
        + self.cuisine_type.title() + " cuisine.")

    def open_restaurant(self):
        """Displays a message indicating if the restaurant is open."""
        print("The " + self.restaurant_name.title() + " is now open.")

johns_place = Restaurant("Jonathan's", "American")
johns_place.describe_restaurant()
johns_place.open_restaurant()
