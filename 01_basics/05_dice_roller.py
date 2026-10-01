import random

# Запрос количества кубиков
dice = int(input("How many dice to roll? "))

for i in range(dice):
    dice_roll = random.randint(1, 6)
    print("Dice result:", dice_roll)
