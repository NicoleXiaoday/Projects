# This is a program that simulate rolling dice.
# The dice is a average 6 sides dice

# Concepts practiced: random, integer, print, while loop

from random import randint
while True:
    ans = input('Would you like to role the dice? (Y/N): ')
    if ans == 'Y':
        num = randint(1,6)
        print('You got: ', num)
    elif ans == 'N':
        break
    else:
        print('Please put a valid input using Y or N')
print('Done!')

