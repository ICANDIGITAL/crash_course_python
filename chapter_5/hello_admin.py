usernames = ['chris', 'kyle', 'admin', 'joker', 'joao']
for username in usernames:
    if username is 'admin':
        print('Hello ' +  username.upper() + ', would you like to see a status report?')
    else:
        print('Hello ' + username.title() + ", thank you for logging in again.")
