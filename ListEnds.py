'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
'''

import random

def first_last(inputList):
    return [inputList[0],inputList[len(inputList)-1]]

if __name__ == '__main__':
    a = []
    list_length = random.randint(2,15)
    while len(a) < list_length:
        a.append(random.randint(1,100))
    print(a)
    print(first_last(a))
