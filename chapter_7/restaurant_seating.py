seating = input("How many people are in your dinner group? ")
seating = int(seating)

if seating >= 8:
    print("You'll have to wait for a table of " + str(seating) + ".")

else:
    print("There is currently a table available.")