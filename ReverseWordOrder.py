'''
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
For example, say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.
'''

def raw_reverse(stringInput):
    listString = stringInput.split()
    result = ''
    for mem in reversed(listString):
        result += mem + ' '
    return result

def reversedString(stringInput):
    return ''.join(stringInput.split()[::-1])

string = input('Enter a string for reversal:\n')
print(raw_reverse(string))
print(reversedString(string))