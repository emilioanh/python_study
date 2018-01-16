from string import ascii_lowercase
from collections import Counter
"""
this is to count the number of each letter in the file
"""
if __name__=="__main__":
    with open('ques.txt') as f:
        print (Counter(letter for line in f 
                    for letter in line.lower() 
                    if letter in ascii_lowercase))
