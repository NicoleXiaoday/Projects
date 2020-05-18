# This is a program that generate a random 
# number between 0-100 
# and lead the user to guess it 

# Concepts practiced: random, integer, print, 
# while loop, if/elif, try except

from random import randint
randnum = randint(0, 100)
print('The random number is: ', randnum)

while True:
    guess = input('Guess the number (0-100): ')
    try:
        if 0 <= int(guess) < (0.5*randnum):
            print('This is way too small!')
            continue
        elif 0 <= int(guess) < randnum:
            print('The guess is too small')
            continue
        elif 100 >= int(guess) > (2*randnum):
            print('This is way too big!')
            continue
        elif 100 >= int(guess) > randnum:
            print('The guess is too big')
            continue
        elif int(guess) == randnum:
            print('You got it!')
            break
        else:
            print('Please input an integer between 0 and 100')
    except:
        print('Please input an integer between 0 and 100')


