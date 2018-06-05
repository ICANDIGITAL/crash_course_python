def cars(manufacturer,model, **details):
    """Displays information about a car."""
    car = {}
    car['Manufacturer: '] = manufacturer.upper()
    car['Model: '] = model.upper()
    for key, value in details.items():
        car[key]=value.upper()
    return car
car_details = cars('bmw','m5', Color='sky blue', Tents='ultra black')
print(car_details)
