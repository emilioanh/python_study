'''
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
'''

def isPrime(number):
    if number==1:
        return True
    elif number==2:
        return False
    #others
    else:
        for divisor in range(3,int(number/2)+1):
            if number % divisor == 0:
                return False
        return True
def get_number(prompt):
    '''Returns integer value for input. Prompt is displayed text'''
    return int(input(prompt))

if __name__ == '__main__':
    while True:
        try:
            if isPrime(get_number('Enter a number to check: ')):
                print('Optimus Prime bitches!')
            else:
                print('Nope!')
        except KeyboardInterrupt as interrupt:
            print('thank you for using!')
            break
        except ValueError as e:
            print('That is not a number please input again!')