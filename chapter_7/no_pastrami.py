print("\nThe deli has ran out of pastrami.\n")
sandwich_orders = []
sandwich_orders.append('grilled cheese')
sandwich_orders.append('tofu veggie')
sandwich_orders.append('incredible')
sandwich_orders.append('pastrami')
sandwich_orders.append('pastrami')
sandwich_orders.append('pastrami')

finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    made_orders = sandwich_orders.pop()
    print("I made your " + made_orders.title() + " sandwich.")
    finished_sandwiches.append(made_orders)

print("\n")

for sandwiches in finished_sandwiches:
    print("The " +  sandwiches.lower() + " sandwich was made.")

