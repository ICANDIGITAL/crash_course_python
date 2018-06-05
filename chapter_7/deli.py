sandwich_orders = []
sandwich_orders.append('grilled cheese')
sandwich_orders.append('tofu veggie')
sandwich_orders.append('incredible')

finished_sandwiches = []

while sandwich_orders:
    made_orders = sandwich_orders.pop()
    print("I made your " + made_orders.title() + " sandwich.")
    finished_sandwiches.append(made_orders)

print("\n")

for sandwiches in finished_sandwiches:
    print("The " +  sandwiches.lower() + " sandwich was made.")

