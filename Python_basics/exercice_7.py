from random import randint

def dice_roller(y, x=1, z=0):
    try:
        x = int(x)
        y = int(y)
        z = int(z)
    except ValueError:
        return "It's not a number"
    dices = [3, 4, 6, 8, 10, 12, 20, 100]
    roll = sum(randint(1, y) for _ in range(1, x)) + z
    for _ in dices:
        if y in dices:
            result = roll * x + z
            return result
        else:
            return 'No such dice'

print(dice_roller(10, 7))