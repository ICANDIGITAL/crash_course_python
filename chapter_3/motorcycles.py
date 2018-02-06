motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
#Below I am employing a totally new method in order to add/append an element to the existing list.
motorcycles.append('nisan')
print(motorcycles)
print(motorcycles[-1].title())
#Below I am building the same list above using the .append() method, starting empty.
motorcycles_2 = []
motorcycles_2.append('honda')
motorcycles_2.append('yamaha')
motorcycles_2.append('suzuki')
print(motorcycles_2)
print(motorcycles_2[1].title())

"""
I learned that there are two distinct ways to build a list.
However the second is more common.
Due to programmers typically not being given all ultimate information at the time of inception.
"""
#Below I am using the .insert method in order to insert an element into a specific place in the list.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'aprillia')
print(motorcycles)

#Below I am using the del statement in order to remove an element from the above live.
del motorcycles[1]
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#Below I am using the .pop() method in order to remove the last element from a list but still work with it.
motorcycles = ['honda', 'yamaha', 'aprillia']
last_owned = motorcycles.pop()
print(motorcycles)
print(last_owned)
print("The last motorcycle that I was advised to buy was an " + last_owned.title() + " " + "two stroke racing bike.")

#Below I am utilizing the .pop() method in order to remow an element from a specific location.
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycles I owned was a " + first_owned.title() + ".")

#Below I wam removing an item from an element, not by indexing, by the actual "value".
#To do this I will be using the .remove() method.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
