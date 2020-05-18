# This is a hangman program, which
# a word is grabbed from a txt file,
# the player guess a single letter
# the player was given limited trials

# Concept practiced: Random, Variables, Boolean
# Integer, Char, String, Length

from random import randint

# Generate a list of words from a txt file
lst = []
fname = open('Hangman.txt')
for line in fname:
    line = line.rstrip()
    words = line.split()
    for word in words:
        lst.append(word)
# Use 'set' data type to remove duplicates
wlst = list(set(lst))
# print (wlst)

# randomly select a word from the list
wordnum = randint(0,(len(wlst)-1))
# print(wordnum)
wordd = wlst[wordnum].lower()
print(wordd)

count = {}
# you can only try 20 times
n = 0

while True:
    gues = input('Guess a letter: ')
    gues = gues.lower()

    # isinstance reture 'True' if specified object is
    # of specified type
    if n >= 20:
        print('You run out of chance...')
        break
    if (len(gues)==1) and 97 <= ord(gues) <= 122:
        if gues not in wordd:
            print('No, its not in the word')
            n = n + 1
            # print (n)
            continue
        else:
            print('Yayy you got one right!')
            n = n + 1
            # print (n)
            count[gues] = count.get(gues, 0) + 1
            # print('disc is: ', count)
            # print('The count of this: letter: ', count[gues])
            # aa = sum(count.values())
            # print('total number of letters guessed right ', aa)
            if sum(count.values()) == len(wordd):
                print('You got all of them!')
                break 
            else:
                continue
    else:
        print('Nahh please input a single letter')
