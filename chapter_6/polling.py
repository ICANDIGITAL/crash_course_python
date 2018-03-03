favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

new_poll = ['chris', 'mohammed', 'kelly', 'shawn', 'phil', 'stephen']

for name in favorite_languages:
    print(name.title() + ", Thank you for responding so swiftly.")

print('\n')
for name in new_poll:
    if name not in favorite_languages:
        print(name.title() + ', we are inviting you to take a special poll.')
