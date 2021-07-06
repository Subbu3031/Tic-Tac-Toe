from IPython.display import clear_output
import random

# to display 3*3 grid board for play
def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])

# grabbing choice of mark for the user
def player_input():
    marker = ' '
    while (marker != 'X' and marker != 'O'):
        marker = input('Player1: Do you want X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    elif marker == 'O':
        return ('O', 'X')

# place the marker on grid chosen by the user
def place_marker(board, marker, position):
    board[position] = marker


# checking all the possible winning conditions
# mark should be placed either horizontally,vertically or diagonally same
def check_win(board, mark):
    h_1 = (board[7] == board[8] == board[9] == mark)
    h_2 = (board[4] == board[5] == board[6] == mark)
    h_3 = (board[1] == board[2] == board[3] == mark)
    v_1 = (board[7] == board[4] == board[1] == mark)
    v_2 = (board[8] == board[5] == board[2] == mark)
    v_3 = (board[9] == board[6] == board[3] == mark)
    d_1 = (board[7] == board[5] == board[3] == mark)
    d_2 = (board[1] == board[5] == board[9] == mark)
    win = (h_1 or h_2 or h_3 or v_1 or v_2 or v_3 or d_1 or d_2)
    return win


# choosing whose turn first
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# checking if the position on grid is empty
def space_check(board, position):
    return board[position] == ' '


# checking if there is no empty space left on grid
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# choosing position to place the mark
def player_choice(board):
    position = 0
    places = range(1, 10)
    while position not in places or space_check(board, position) == False:
        position = int(input('Choose your next position 1 to 9: '))
    return position


# if user want to replay the game
def replay():
    return input('Do you want to play again? Y or N: ').lower().startswith('y')


# starting the game
print('WELCOME TO TIC TAC TOE GAME!')
while True:
    theBoard = [' '] * 10

    # get the marks for the respective players
    player1_mark, player2_mark = player_input()

    # choosing whose turn first randomly
    turn = choose_first()
    print(turn + ' will go first.')

    # ask whether to start or end, if yes continue or else end the game
    play_game = input('Are you ready to play? Y or N.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    # if yes to play the game, starting with the turns
    # initially display the board and let the player choose the empty position on grid
    # then place the respective marker on the grid
    # check the win condition. If yes, stop the game and return the winner
    # and also check if the game is tie without any empty positions
    # if none of these cases succeed, then change the turn of the player
    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_mark, position)
            if check_win(theBoard, player1_mark):
                display_board(theBoard)
                print('Congratulations, Player 1 won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_mark, position)
            if check_win(theBoard, player2_mark):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is draw!')
                    break
                else:
                    turn = 'Player 1'

    # asking the user if he wants to replay
    if not replay():
        break