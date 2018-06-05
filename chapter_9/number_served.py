class Restaurant():
    """Stores attributes of a restaurant."""
    def __init__(self, restaurant_name, cusine_type):
        """Initializing name and cusine attributes."""
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes the restaurants details."""
        print("The name of this restaurant is: ")
        print(self.restaurant_name.upper() +"\n")
        print("The cusinse type of this restaurant is: ")
        print(self.cusine_type.title())

    def open_restaurant(self):
        """Print a message stating if the restaurant is open."""
        print("The " + self.restaurant_name.title() + " is now open.")

    def set_number_served(self, customers):
        """Logs the numbers of customers that have been served."""
        self.number_served = customers

    def increment_number_served(self, current_customers):
        """Updates the number of cuastomers that have been served."""
        self.number_served += current_customers



restaurant = Restaurant("Chocolate Factory","Candy")

print(restaurant.number_served)
restaurant.number_served += 25
print(restaurant.number_served)

restaurant.set_number_served(30)
print(restaurant.number_served)

restaurant.increment_number_served(500)
print(restaurant.number_served)

restaurant.increment_number_served(10)
