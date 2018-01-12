'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random

while True:
    isExit = False
    turn = 1
    randNum = random.randint(1,9)
    while True:
        print(randNum)
        guess = input('Enter your number: ')
        if guess.lower() in ['exit','Exit','EXIT']:
            isExit = True
            break
        elif int(guess) < randNum:
            print('The number you enter is lower than expected!')
        elif int(guess) > randNum:
            print('The number you enter is higher than expected!')
        elif int(guess) == randNum:
            if turn < 2:
                print('Fucking genius, the number you enter is exactly right, and only on the first try!')
            elif turn < 10:
                print('A little stupid but ok, you rock it after {} tries'.format(turn))
            else:
                print('Finally, you stupid ass bitch guess it right. Your attempts:', turn)
            break
        turn+=1
    if isExit == False:
        choice = input('Wanna play more, if no type "exit"? ')
        if choice in ['exit','Exit','EXIT']:
            isExit = True
    if isExit == True:
        print('Scared of a little game, what a coward! Hahaha')
        break