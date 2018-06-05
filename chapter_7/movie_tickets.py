age = input("What is you age?")
age = int(age)

if age < 3:
    print("The ticket is free.")
elif age <= 12:
    print("The ticket will cost your parents $10.")
else:
    print("The ticket will cost you $15.")