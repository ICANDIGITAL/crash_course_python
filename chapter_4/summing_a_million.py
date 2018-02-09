#List Comprehension Method
money_counter = [top_dollar for top_dollar in range (1, 1000001)]
print(min(money_counter))
print(max(money_counter))
print(sum(money_counter))

#Loop Method
money_counter = []
for money in range(1,1000001):
    count = money
    money_counter.append(count)
print(min(money_counter))
print(max(money_counter))
print(sum(money_counter))
