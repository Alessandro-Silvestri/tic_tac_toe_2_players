'''
TIC TAC TOE game (2 human players)

player 1 has this symbol: "X"
player 1 has this symbol: "O"

Solved by Alessandro Silvestri 2024 <alessandro.silvestri.work@gmail.com>
'''

def show_board():
    '''show the board updated'''
    print(f"+-----+-----+-----+")
    print(f"|  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  |")
    print(f"|-----|-----|-----|")
    print(f"|  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  |")
    print(f"|-----|-----|-----|")
    print(f"|  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  |")
    print(f"+-----+-----+-----+")

def insert_symbol(position:int, symbol:str):
    '''insert 'X' or 'O' in the right position in the board '''
    index = 0
    exit = False
    for i in board:
        index1 = 0
        for j in i:      
            if j == position:
                board[index][index1] = symbol
                exit = True
                break
            index1 += 1   
        index += 1
        if exit:
            break

def result_comparation(): # bool
    '''check if there is a completed line'''
    return board[0][0] == board[0][1] and board[0][0] == board[0][2] or \
        board[1][0] == board[1][1] and board[1][0] == board[1][2] or \
        board[2][0] == board[2][1] and board[2][0] == board[2][2] or \
        board[0][0] == board[1][0] and board[0][0] == board[2][0] or \
        board[0][1] == board[1][1] and board[0][1] == board[2][1] or \
        board[0][2] == board[1][2] and board[0][2] == board[2][2] or \
        board[0][0] == board[1][1] and board[0][0] == board[2][2] or \
        board[2][0] == board[1][1] and board[2][0] == board[0][2]
        
def check_is_draw(): # bool
    '''check if in the board there are still available position to play'''
    draw = False
    for i in board:
        for j in i:
            if j == "O" or j == "X":
                continue
            else:
                draw = True
                break
        if draw:
            break              
    return not draw

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
allowed_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
show_board()
draw = False

# game
while True:
    # player 1 move
    palyer1_playing = True
    while True: 
        # check valid input 
        player_choice = input("Player 1: 'X' > ").upper()
        if player_choice not in allowed_choices:
            print("wrong input")
            continue
        break
    insert_symbol(int(player_choice), "X")
    show_board()
    if result_comparation():
        break
    if check_is_draw():
        draw = True
        break

    # player 2 move 
    palyer1_playing = False
    while True:
        # check valid input
        player_choice = input("Player 2: 'O' > ").upper()
        if player_choice not in allowed_choices:
            print("wrong input")
            continue
        break
    insert_symbol(int(player_choice), "O")
    show_board()
    if result_comparation():
        break
    if check_is_draw():
        draw = True
        break

# print result
if draw:
    print("DRAW")
elif palyer1_playing:
    print("Player1 WON!")
else:
    print("Player2 WON!")
    

