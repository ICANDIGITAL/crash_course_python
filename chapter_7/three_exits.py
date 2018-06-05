prompt = "Which toppings would you like to order on your pizza guys?"
prompt += "\nEnter quit to exit: "

# Conditional While statement:
while True:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print("I'll be adding the " + toppings.lower() + " shortly.")


# Active variable:
active = True
toppings = input(prompt)
if toppings == "quit":
    active = False
print("I'll be adding the " + toppings.lower() + " shortly.")




# Break statement example:
while True:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print("I'll be adding the " + toppings.lower() + " shortly.")