from random import randint


class Dice:
    """Print values for a dice roll."""
    def __init__(self, sides=6):
        """Initialize attribute."""
        self.sides = sides

    def roll_dice(self):
        """Returns a random value received from a 6-sided dice roll."""
        return randint(1, self.sides)


d6 = Dice()

results = []
for roll_num in range(10):
    result = d6.roll_dice()
    results.append(result)
print("10 rolls of a 6-sided dice:")
print(results)


d10 = Dice(sides=10)

ten_sided_results = []
for roll_num in range(10):
    ten_sided_result = d10.roll_dice()
    ten_sided_results.append(ten_sided_result)
print("\n")
print("10 rolls of a 10-sided dice:")
print(ten_sided_results)

d20 = Dice(sides=20)

twenty_sided_results = []
for roll_num in range(10):
    twenty_sided_result = d20.roll_dice()
    twenty_sided_results.append(twenty_sided_result)
print("\n")
print("10 rolls of a 20-sided dice:")
print(twenty_sided_results)
