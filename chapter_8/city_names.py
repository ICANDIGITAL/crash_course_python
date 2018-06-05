def city_country(city,country):
    """Displays the city and country of a place."""
    location = (city.title() + ", " + country)
    return location

cool_place_1 = city_country('rio de janeiro', 'Brazil')
cool_place_2 = city_country('new york', 'USA')
cool_place_3 = city_country('lison', 'portugal')

print(cool_place_1)
print(cool_place_2)
print(cool_place_3)
