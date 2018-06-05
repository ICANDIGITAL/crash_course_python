class Restaurant():
    """Stores attributes of a restaurant."""
    def __init__(self, restaurant_name, cusine_type, *flavors):
        """Initializing name and cusine attributes."""
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.flavors = flavors

    def describe_restaurant(self):
        """Describes the restaurants details."""
        print("The name of this restaurant is: ")
        print(self.restaurant_name.upper() +"\n")
        print("The cusinse type of this restaurant is: ")
        print(self.cusine_type.title())

    def open_restaurant(self):
        """Print a message stating if the restaurant is open."""
        print("The " + self.restaurant_name.title() + " is now open.")

    def types_of_flavors(self):
        """Displays a list of flavors served."""
        print("The following flavors are availible:")
        for flavor in self.flavors:
            print("- " + flavor.title())
