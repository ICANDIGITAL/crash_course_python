filename = 'GMU Letter.txt'
with open(filename) as fileobject:
    lines = fileobject.read()

print("Count for life: " + str(lines.count('life')))
print("Count for life.lower(): " + str(lines.lower().count('life')))
