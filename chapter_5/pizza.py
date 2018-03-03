#Below I am learning how to store a list inside a dictionary.
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushroom', 'extra cheese'],
}

print('You ordered a ' + pizza['crust'] + '-crust pizza ' +
'with the following toppings:')
for topping in pizza['toppings']:
    print('\t' + topping)
