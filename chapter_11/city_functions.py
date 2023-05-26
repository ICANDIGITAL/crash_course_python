def city_country(city, country, population=0):
    """Returns a city and country seperated by a comma in title case."""
    if population > 0:
        correct_format = city + ', ' + country + " - " + str(population)
        return correct_format.title()
    else:
        correct_format = city + ', ' + country
        return correct_format.title()

