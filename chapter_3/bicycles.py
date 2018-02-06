#NAME: Christopher Leader DATE: 04/01/2018 DESCRIPTION: Below I am learning how to make lists.
bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)
#The list item start at 0 not 1. Therefore, to pull an item subtract it's place by one.
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[3].title())
#Here I am learning how to access the items in the list in reverse by using the - sign.
print(bicycles[-1].title())
print(bicycles[-2].title())
print(bicycles[-3].title())
#Note that you can always access the last item in a list by inputing [-1]. As done above.
#Below I am using concatenation to create a message with an item from the list.
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
