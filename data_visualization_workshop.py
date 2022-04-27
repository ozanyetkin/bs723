import random
import matplotlib.pyplot as plt

dice_faces = [1, 2, 3, 4, 5, 6]

number_of_rolls = 10
number_of_dice = 10

all_totals = []
for i in range(number_of_rolls):
    # round_results = []
    round_total = 0
    for m in range(number_of_dice):
        dice_result = random.choice(dice_faces)
        # round_results.append(dice_result)
        round_total = round_total + dice_result
    all_totals.append(round_total)

fig, ax = plt.subplots()
ax.scatter(x=range(number_of_rolls), y=all_totals)
ax.set_ylim([number_of_rolls * min(dice_faces), number_of_rolls * max(dice_faces)])
plt.show()

plt.hist(all_totals, bins=len(all_totals), range=(number_of_rolls * min(dice_faces), number_of_rolls * max(dice_faces)))
plt.show()