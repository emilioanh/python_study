from DrawAGameBoard import draw_board

def switch_cur_player(cur_player):
    if cur_player==1:
        return 2
    return 1

if __name__ == "__main__":
    size = int(input("input the size of the Tic Tac Toe: "))
    game = [[' ' for i in range(size)] for j in range(size)]
    unmarked_spots = size*size
    cur_player = 1
    while unmarked_spots>0:
        draw_board(size, game)
        print("Current player "+ str(cur_player) +" turn!")
        coordinate = input("input the coordinate of your choice (row,column): ")
        user_tick = [coordinate.split(",")[0], coordinate.split(",")[1]]
        print(user_tick)
        cur_player = switch_cur_player(cur_player)
        print(cur_player)
        unmarked_spots = 0