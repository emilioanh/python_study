'''
This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

The original formulation of this exercise said to write the solution using one line of Python, but a few readers pointed out that this was impossible to do without using sets that I had not yet discussed on the blog, so you can either choose to use the original directive and read about the set command in Python 3.3, or try to implement this on your own and use at least one list comprehension in the solution.

Extra:

Randomly generate two lists to test this
'''

import random

# a = []
# list_length = random.randint(2,15)
# while len(a) < list_length:
#     a.append(random.randint(1,100))
# b = []
# list2_length = random.randint(2,15)
# while len(b) < list2_length:
#     b.append(random.randint(1,100))
# c = random.sample(range(1,90),12) #random.sample(range(number to start random, number to end),number of element)
# print(c)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result = []
# result.append(set(a).intersection(b))
#set has intersection method not list
result = [index for index in set(a) if index in b]
print(result)