#
#  1 | 2 | 3
# -----------
#  4 | 5 | 6
# -----------
#  7 | 8 | 9

#Draw playground

board = {
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " ",
}


def choose_number(player):
    keep_asking = True
    while keep_asking:
        chosen_number = int(input(f"{player}: Choose number 1-9: "))
        if chosen_number not in board:
            print("Wrong number. Try it again.")
        elif board[chosen_number] == " ":
            board[chosen_number] = player
            keep_asking = False
        else:
            print("Number already taken. Try it again.")

def draw_field(board):
    field = (f"\n"
        f" {board[1]} | {board[2]} | {board[3]} \n"
        f"{11 * '-'}\n"
        f" {board[4]} | {board[5]} | {board[6]} \n"
        f"{11 * '-'}\n"
        f" {board[7]} | {board[8]} | {board[9]} ")
    return field

def score_check(board, player):
    if ((board[1] == board[2] == board[3] == player) or
        (board[4] == board[5] == board[6] == player) or
        (board[7] == board[8] == board[9] == player) or
        (board[1] == board[4] == board[7] == player) or
        (board[2] == board[5] == board[8] == player) or
        (board[3] == board[6] == board[9] == player) or
        (board[1] == board[5] == board[9] == player) or
        (board[3] == board[5] == board[7] == player)):
        print(f'Player "{player}" wins!')
        return True
    else:
        return False

def replay():
    play_again = input("Do you want to play again (y/n)?: ")
    if play_again.lower() == "y":
        return True
    elif play_again.lower() == "n":
        return False

def play_game():
    print('Welcome to Tic Tac Toe game.')
    player_2 = None
    while not player_2:
        player_1 = input('Choose "X" or "O" symbol: ')
        if player_1 == "X":
            player_2 = "O"
        elif player_1 == "O":
            player_2 = "X"
        else:
            print("Wrong symbol. Try it again.")
    print(f'Player 1: "{player_1}", player 2: "{player_2}"')
    round = 1
    game_on = True
    while game_on:
        if round <= 9:
            if round % 2 == 0:
                choose_number(player_1)
                print(draw_field(board))
                if score_check(board, player_1):
                    game_on = False
                    break
            else:
                choose_number(player_2)
                print(draw_field(board))
                if score_check(board, player_2):
                    game_on = False
                    break
        else:
            print("Draw!")
            game_on = False
        round += 1

play_game()
