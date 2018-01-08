"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""


divisors = []
while True:
    try:
        num = int(input('please input the number u want to find divisors:'))
        break
    except ValueError as e:
        print("Oops!  That was no valid number.  Try again...")
for i in range(1,num):
    if num%i==0:
        divisors.append(i)
print(divisors[0:])