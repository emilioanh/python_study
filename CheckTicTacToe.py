'''
If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won
'''

game = [
    [0,2,2],
    [1,2,1],
    [2,0,1]]
row_set = ()

def check_row(game, size):
	for i in range(size):
		row_set = set(game[i]) #a set can not have duplicated elements
		if len(row_set) == 1 and game[i][0] != 0:
			return game[i][0]
	return 0

def transpose_matrix(matrix):
    trans_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return trans_matrix

def diagonal_match(game, size):
    if game[0][0] != 0 :
        match_count = 0
        for i in range(size-1):
            if game[i][i]==game[i+1][i+1]:
                match_count += 1
        if match_count==size-1:
            return game[0][0]
    if game[0][size - 1] != 0:
        match_count = 0
        for i in range(size-1):
            if game[i][size-1-i]==game[i+1][size-2-i]:
                match_count += 1
        if match_count==size-1:
            return game[0][size - 1]             
    return 0

if check_row(game, 3) > 0:			
	print (str(check_row(game, 3)) + str(" row wins!"))
transposed = transpose_matrix(game)
if check_row(transposed, 3) > 0:			
	print (str(check_row(transposed, 3)) + str(" column wins!"))
if diagonal_match(game, 3) > 0:
	print (str(diagonal_match(game, 3)) + str(" diagonal wins!"))