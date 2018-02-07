pretty_girls = []
pretty_girls.append('jalisa')
pretty_girls.append('jackie')
pretty_girls.append('silvia')
pretty_girls.append('vanity')
print(pretty_girls)

pretty_girls.insert(1, 'brigette')
print(pretty_girls)

del pretty_girls[-2]
print(pretty_girls)

already_taken = pretty_girls.pop()
print(pretty_girls)

pretty_girls.remove('jalisa')
print(pretty_girls)

pretty_girls.sort()
print(pretty_girls)

print(sorted(pretty_girls, reverse = True))

pretty_girls.remove('brigette')
print(pretty_girls[0].title())

print(len(pretty_girls))
