'''
Write a program that asks the user how many Fibonnacci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the
previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

def Fibonnaci(numSeq):
    if numSeq==1:
        return 1
    elif numSeq==2:
        return 1
    else:
        return Fibonnaci(numSeq-1)+Fibonnaci(numSeq-2)
        
if __name__ == '__main__':
    while True:
        try:
            numSeq = int(input('Enter how many Fibonnacci you want to generate: '))
            break
        except ValueError as e:
            print("Oops!  That was no valid number.  Try again...")
    for numOrd in range(1,numSeq+1):
        print(Fibonnaci(numOrd), end=',')