#Instructions:
# 1. Download Python base code: https://www.python.org/
# 2. Download Pycharm IDE: https://www.jetbrains.com/pycharm/
# 3. Add this file to Pycharm and run program therein!


import random

rolls = []

def roll_dice(num):
    rolls.append(random.randint(1, num))

dice_type = input("Enter die size (i.e. d4, d6, etc.): ")
num_rolls = int(input("How many times do you want to roll? "))

if dice_type == ("d4"):
    for i in range(num_rolls):
        roll_dice(4)

elif dice_type == ("d6"):
    for i in range(num_rolls):
        roll_dice(6)

elif dice_type == ("d8"):
    for i in range(num_rolls):
        roll_dice(8)

elif dice_type == ("d10"):
    for i in range(num_rolls):
        roll_dice(10)

elif dice_type == ("d12"):
    for i in range(num_rolls):
        roll_dice(12)

elif dice_type == ("d20"):
    for i in range(num_rolls):
        roll_dice(20)

elif dice_type == ("d100"):
    for i in range(num_rolls):
        roll_dice(100)
else:
    print("Invalid Input. Try not to be dumb next time!")

print(rolls))
print("Total: " + str(sum(rolls))