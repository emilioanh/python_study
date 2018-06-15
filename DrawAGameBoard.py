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

def print_slash(size):
    print('|   '*(size+1))

if __name__ == "__main__":
    size = int(input("Enter the size of the board:"))
    for index in range(size):
        print_dash(size)
        print_slash(size)
    print_dash(size)