#Directly below I am using the loop method.
a_million = []
for million in range(1, 1000001):
    jay_z = million
    a_million.append(jay_z)
    print(a_million)

#Alternatively, I can use the list comprehension method.
a_million = [jay_z for jay_z in range(1, 1000001)]
print(a_million)
