import random
import matplotlib.pyplot as plt

sides = [1, 2, 3, 4, 5, 6]

def roll_dice(sides):
    dice = random.choices(sides, weights=[1, 10, 1, 1, 1, 1], k=1)
    return dice[0]

num_of_rolls = 100
num_of_dices = 1000
sum_of_results = []
for i in range(num_of_rolls):
    results = 0
    for d in range(num_of_dices):
        result = roll_dice(sides)
        # print(result)
        results += result
    # print(results)
    sum_of_results.append(results)

range_min = num_of_dices * sides[0]
range_max = num_of_dices * sides[-1]

fig, ax = plt.subplots()

ax.scatter(range(num_of_rolls), sum_of_results)
ax.set(ylim=(range_min, range_max))

plt.show()

plt.hist(sum_of_results, bins=len(sum_of_results), range=(range_min, range_max))
plt.show()
