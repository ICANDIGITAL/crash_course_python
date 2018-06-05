print('\nThis program will add two numbers together.')
print('Enter \'q\' to quit.')

while True:
    first_number = input("\nEnter First Number Here: ")
    if first_number == 'q':
        break
    second_number = input("Enter Second Number Here: ")
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Sorry, you can only enter numbers.")
    else:
        print("The answer is: " + str(answer))