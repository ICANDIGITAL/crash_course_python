from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """A simple attempt at modeling an ice cream stand."""

    def __init__(self, restaurant_name, cusine_type, flavors):
        """
        Initialize the attributes of the parent class.
        Then initialize the attribute specific to a ice cream stand.
        """
        super().__init__(restaurant_name, cusine_type, flavors)

ice_box = Restaurant("The Ice Box", "Ice Cream", 'chocolate', 'rainbow', 'cookie doough'

ice_box.types_of_flavors()
