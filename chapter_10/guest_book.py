filename = 'guest_book.txt'

prompt = ('Hello user, what is your name?\n')
prompt += ('Enter \'q\' to quit: ')


while True:
    user_name = input(prompt)

    if user_name == 'q':
        break
    else:
        print('\n' + user_name.upper() + '! ' + 'Welcome your majesty!\n')
        with open(filename, 'a') as file_object:
            file_object.write(user_name + "\n")



