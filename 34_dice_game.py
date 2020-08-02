# Dice_Game
import random


def dice():
    z = ''
    while z != 'quit':
        z = input('P1s turn. Press enter: ')
        if z != "quit":
            first = random.randint(1, 6)
            print(first)
        else:
            print('bye')
            break
        z = input('P2s turn. Press enter: ')
        if z != "quit":
            second = random.randint(1, 6)
            print(second)
        else:
            print('bye')


dice()

