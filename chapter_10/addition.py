prompt = 'Enter two numbers to add them bellow.'
prompt += 'Type \'q\' to quit.'

first_number = input('Enter first number here: ')
second_number = input('Enter second number here: ')
try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("You can only add numbers in this program sweetie.")
else:
    print("The answer is: " + str(answer))

