#Below I am importing a function from a module.
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n')

#Below I am importing a function from a module using an alias VIA "as".
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#Below I am giving a module an alias VIA "as".
import pizza as p

p.make_pizza(6, 'black mamba')

#Below I am importing every function from a module by using an "*".
#NOTE: This style is the least optimal of all four.
from pizza import *

make_pizza(4,'king cobra')
