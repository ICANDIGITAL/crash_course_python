my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for foods in my_foods:
    print(foods)

print("\nMy friend's favorite foods are:")
for friend in friend_foods:
    print(friend)
