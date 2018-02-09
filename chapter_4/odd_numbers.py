#List Comprehension Method
num = [odd for odd in range(1, 21, 2)]
print(num)

#Loop Method *Note: You have to make sure that the print function is not indented.
num = []
for odd in range(1, 21, 2):
    skip = odd
    num.append(skip)
print(num)
