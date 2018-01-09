"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""

import random

numlist = []
list_length = random.randint(5,15)
while len(numlist) < list_length:
    numlist.append(random.randint(1,1000))
print(numlist)
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [num for num in numlist if num%2==0]
"""
above code line equal:
for num in numlist:
    if num%2==0:
        b.append(num)
"""
print(b)