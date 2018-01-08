"""
write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python 
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# s2 = set(b)
# c = [val for val in a if val in s2]
c = []
if ((a>b)-(a<b))>=0:
    for i in b:
        if i in a:
           if i not in c:
               c.append(i)
else:
    for i in a:
        if i in b:
            if i not in c:
               c.append(i)
print(c[0:])