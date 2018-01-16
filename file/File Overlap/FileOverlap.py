'''
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
(If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics -
you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)
'''
import time
start_time = time.time()
with open('primenumbers.txt','r') as f:
    allPrime = f.readlines()
    for index in range(0,len(allPrime)-1):
        allPrime[index] = allPrime[index].strip()
with open('happynumbers.txt','r') as ofile:
    allHappy = ofile.readlines()
    for index in range(0,len(allHappy)-1):
        allHappy[index] = allHappy[index].strip()   
overLap = [value for value in allPrime if value in allHappy]
print(overLap)
print("--- %s seconds ---" % (time.time() - start_time))