import json


def get_stored_number():
    """A function that ask a user for their favorite number."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def stored_number():
    """A function that prints users favorite number."""
    favorite_number = get_stored_number()
    if favorite_number:
        print("I know your favorite number it's " + str(favorite_number)+".")
    else:
        favorite_number = input('Human input your favorite number here: ')
        filename = 'favorite_number.json'
        with open(filename, 'w') as f_obj:
            json.dump(favorite_number, f_obj)
            print("Human your favorite number is now stored...")


stored_number()
