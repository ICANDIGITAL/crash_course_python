rivers = {
    'nile' : 'egypt',
    'mississippi' : 'usa',
    'amazon' : 'brazil'
}

for river, country in sorted(rivers.items()):
    print('The ' + river.title() + ' runs through ' + country.title() + '.' )

print('\n')
for river in sorted(rivers.keys()):
    print(river.title())

print('\n')
for country in sorted(rivers.values()):
    print(country.upper())
