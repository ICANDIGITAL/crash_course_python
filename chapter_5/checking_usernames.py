current_users = ['chris', 'kyle', 'admin', 'joker', 'joao']
new_users = ['chris', 'steven', 'matt', 'hacker', 'Joao']
current_users = [element.lower() for element in current_users]
new_users = [element.lower() for element in new_users]
for username in new_users:
    if username in current_users:
        print(username + ", you have to pick another name.")
    if username not in current_users:
        print(username + ", this name is available.")
