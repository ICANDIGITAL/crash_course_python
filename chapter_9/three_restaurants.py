class Restaurant():
    """Stores attributes of a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initializing name and cuisine attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes the restaurants details."""
        print("The name of this restaurant is: ")
        print(self.restaurant_name.upper() + "\n")
        print("The cuisine type of this restaurant is: ")
        print(self.cuisine_type.title())

    def open_restaurant(self):
        """Print a message stating if the restaurant is open."""
        print("The " + self.restaurant_name.title() + " is now open.")


restaurant = Restaurant("Chocolate Factory", "Candy")
johns_place = Restaurant("Burt McGurt's", "Country")
matts = Restaurant("White Pepper", "Italian")

print(restaurant.restaurant_name.upper())
print(restaurant.cuisine_type.lower())
print("\n")

restaurant.describe_restaurant()
print("\n")
restaurant.open_restaurant()

print("\n")
johns_place.describe_restaurant()

print("\n")
matts.describe_restaurant()
