'''
This time, we’re going to do exactly the opposite. You, the user, will have in your head 
a number between 0 and 100. The program will guess a number, and you, the user, will say 
whether it is too high, too low, or your number.
At the end of this exchange, your program should print out how many guesses it took to get 
your number.
'''
import random

guess_number = 50
big_range = 100
small_range = 0
attempt = 0

while True:
    print('Is this your number (yes/bigger/smaller): ', guess_number)
    attempt += 1
    answer = input('Answer: ')
    if answer.lower() in ['yes', 'y']:
        print(f'I beat ya dog, your attempts were {attempt} ')
        break
    elif answer.lower() == "bigger":
        small_range = guess_number
        guess_number = int((guess_number + big_range)/2)
        # guess_number = random.randint(guess_number + 1, big_range - 1)
    else :
        big_range = guess_number
        guess_number = int((small_range + guess_number)/2)
        # guess_number = random.randint(small_range + 1, guess_number - 1)
    print('fuck u with ya number, I will not give up!')