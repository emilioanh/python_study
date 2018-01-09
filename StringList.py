"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""
stringInput = input('Enter a string to check: ')
if stringInput[::-1] == stringInput:
    print('This string is a palindrome string!')
else:
    print('Nope, not palindrome!')