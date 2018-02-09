pizzas  = ['extra cheese', 'veggie', 'pan']
friend_pizzas = pizzas[:]
pizzas.append('white')
friend_pizzas.append('supreme')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for neighbor_pizza in friend_pizzas:
    print(neighbor_pizza)
