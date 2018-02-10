keep_count = list(range(0,10))
for number in keep_count:
    if number < 2:
        print(str(number) + "st")
    elif number < 3:
        print(str(number) + "nd")
    elif number < 4:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
