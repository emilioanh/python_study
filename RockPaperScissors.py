'''
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input),compare them,print out a message of congratulations to the winner,
and ask if the players want to start a new game)
Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''

class UserRPS(object):
    name = ''
    option = ''
    def __init__(self):
        self.inputName()
        self.inputOption()
    def inputName(self):
        self.name = input("What's your name?\n")
    def inputOption(self):
        self.option = input('{0}, do yo want to choose rock, paper or scissors?\n'.format(self.name))

def compare(u1, u2):
    if u1.option.lower() == u2.option.lower():
        return("It's a tie!")
    elif u1.option.lower() == 'rock' and (u2.option.lower() in ['rock','paper','scissors']):
        if u2.option.lower() == 'scissors':
            return('{0} wins!'.format(u1.name))
        else:
            return('{0} wins!'.format(u2.name))
    elif u1.option.lower() == 'scissors' and (u2.option.lower() in ['rock','paper','scissors']):
        if u2.option.lower() == 'paper':
            return('{0} wins!'.format(u1.name))
        else:
            return('{0} wins!'.format(u2.name))
    elif u1.option.lower() == 'paper' and (u2.option.lower() in ['rock','paper','scissors']):
        if u2.option.lower() == 'rock':
            return('{0} wins!'.format(u1.name))
        else:
            return('{0} wins!'.format(u2.name))
    else:
        return('Invalid input! You have not entered rock, paper or scissors, try again.')

if __name__ == '__main__':
    while True:
        u1 = UserRPS()
        u2 = UserRPS()
        print(compare(u1,u2))
        choice = input('Do you want to continue(y/n)? ')
        if(choice in ['n','N'] or 'no' in choice.lower()):
            break

# print(compare(user1_answer, user2_answer))
# def abc():
#     sub1='pikachu'
#     return('i am a {0}'.format(sub1))

# print(abc())