'''
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and
another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
Extras:
Use binary search.
'''

import random

def find(ordered_list, number):
    start_index = 0
    end_index = len(ordered_list) - 1
    while start_index <= end_index:
        middle_index = int((end_index + start_index) / 2)
        middle_element = ordered_list[middle_index]
        if middle_element == number:
            return True
        elif number > middle_element:
            start_index = middle_index + 1
        else:
            end_index = middle_index - 1
    return False
  
if __name__=="__main__":
    l = random.sample(range(1,100),7)
    l.sort()
    print(l)
    print(find(l,55))

