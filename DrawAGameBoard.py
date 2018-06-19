'''
Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
'''

def print_dash(size):
    print(' ---'*size)

def print_slash(size, row):
    for i in range(size):
        print('| '+ row[i] +' ', end='')
    print('|')

def draw_board(size, game):
    for index in range(size):
        print_dash(size)
        print_slash(size,game[index])
    print_dash(size)

if __name__ == "__main__":
    game = [
    ['X','X','O'],
    ['O','O','X'],
    ['O','X','O']]
    size = int(input("Enter the size of the board:"))
    for index in range(size):
        print_dash(size)
        print_slash(size,game[index])
    print_dash(size)