prompt = "Which toppings would you like to order on your pizza guys?"
prompt += "\nEnter quit to exit: "


while True:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print("I'll be adding the " + toppings.lower() + " shortly.")