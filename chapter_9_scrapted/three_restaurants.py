class Restaurant():
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisinse attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Dsiplays a discription of the restaurant."""
        print("The " + self.restaurant_name.title() + "'s serves a "
        + self.cuisine_type.title() + " cuisine.")

    def open_restaurant(self):
        """Displays a message indicating if the restaurant is open."""
        print("The " + self.restaurant_name.title() + "'s is now open.")

johns_place = Restaurant("Jonathan", "American")
burts_place = Restaurant("Burt", "Country")
j_boogie = Restaurant("J. Boogie", "Southern")
johns_place.describe_restaurant()
burts_place.describe_restaurant()
j_boogie.describe_restaurant()
print("\n")
johns_place.open_restaurant()
