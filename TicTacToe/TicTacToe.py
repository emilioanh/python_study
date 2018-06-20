from DrawAGameBoard import draw_board
from CheckTicTacToe import check_tic_tac_toe
import random

cheer_list = ["Nice one", "Cool, keep on", "What a move"]

def switch_cur_player(cur_player):
    if cur_player==1:
        return 2
    return 1

if __name__ == "__main__":
    size = int(input("input the size of the Tic Tac Toe: "))
    game = [[' ' for i in range(size)] for j in range(size)] #init ' ' 2 dimension array
    unmarked_spots = size*size
    cur_player = 1
    while unmarked_spots>0:
        draw_board(game, size)
        print("Current player "+ str(cur_player) +" turn!")
        coordinate = input("input the coordinate of your choice start with 1 (row,column): ")
        user_tick = [int(coordinate.split(",")[0]), int(coordinate.split(",")[1])]
        if game[user_tick[0]-1][user_tick[1]-1] == ' ':
            if cur_player == 1:
                game[user_tick[0]-1][user_tick[1]-1] = 'X'
            else:
                game[user_tick[0]-1][user_tick[1]-1] = 'O'
            unmarked_spots -= 1
            result = check_tic_tac_toe(game, size)
            if result == 1:
                print("player 1 win")
                draw_board(game, size)
                break
            elif result == 2:
                print("player 2 win")
                draw_board(game, size)
                break
            print(random.choice(cheer_list))
            cur_player = switch_cur_player(cur_player)
        else:
            print("You cannot select checked spot!")
    print("It's a draw")
    draw_board(game, size)