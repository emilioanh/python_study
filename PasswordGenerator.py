'''
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.
Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symb = '!@#$%^&*()-_[]./\,'
words = 'This Password Is For Idiot'.split()
password = ''
if(str.lower(input('Do you want a Strong or Weak Password?: ')) == 'strong'):
    pwdLength = int(input('How long do you want your password? '))
    while len(password) < pwdLength:
        temp = random.randint(1,3)
        if temp == 1:
            password += lower[random.randint(0,len(lower)-1)]
        elif temp == 2:
            password += upper[random.randint(0,len(upper)-1)]
        else:
            password += symb[random.randint(0,len(symb)-1)]
    print(password)
else:
    password += words[random.randint(0,len(words)-1)] + words[random.randint(0,len(words)-1)]
    print(password)
    