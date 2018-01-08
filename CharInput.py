"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines
"""

import datetime

now = datetime.datetime.now()
while True:
    try:
        name = input('Enter your name:')
        age = int(input('Enter your age:'))
        year_100 = now.year - age +100
        numTime = int(input('Enter how many time:'))
        for i in range(numTime):
            print(f"Hi {name} you'll be 100 in {year_100}!")
        break
    except ValueError as e:
        print("Oops!  That was no valid number.  Try again...")
