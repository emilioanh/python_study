"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

while True:
    try:
        check = int(input('Enter a number:'))
        num = int(input('enter the number you want to divide to:'))
        break
    except ValueError as e:
        print("Oops!  That was no valid number.  Try again...")
if check%num==0:
    print(f'{check} is fully divided to {num}')
else:
    print(f'{check} is not a multiple of {num}')