user_name = input('User please enter your name here: ')

filename = "guest.txt"
with open(filename, 'w') as file_object:
    file_object.write(user_name)