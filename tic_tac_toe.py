
# Imports
import os
import time


# Defining the board
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]


# game instructions
def game_instructions():
    print("                     TIC TAC TOE.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("This game requires two players. Player \"X\" and Player \"O\"")
    print()
    print("  |  |  ")
    print(""+"1"+" |"+"2 "+"| "+"3"+" ")
    print("--|--|--")
    print(""+"4"+" |"+"5 "+"| "+"6"+" ")
    print("--|--|--")
    print(""+"7"+" |"+"8 "+"| "+"9"+" ")
    print("--|--|--")
    print()
    print("The empty spaces below are represented using the above numbers.")
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                     GAME IN PROGRESS...                       ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# print the board
def print_board():
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print("   |   |   ")
    print("---|---|---")
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
    print("   |   |   ")
    print()


# function to check if "X" or "O" is winner
# takes two parameters "board --> the board it's self" AND "player --> for either X or O"
def is_winner(board, player):
    if board[1] == player and board[2] == player and board[3] == player or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
            (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False


# function to check for a Tie between O and X
def is_board_full(board):
    if " " in board:
        return False
    else:
        return True

# creating the main loop using while.


while True:
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Player X
    os.system('clear')
    game_instructions()
    print_board()

    # getting user input
    global choiceX
    try:
        choiceX = int(input("Please choose an empty space for X."))
    except IndexError:
        print("Invalid Number!!!")
    except ValueError:
        print("Invalid Number!!!")
    except NameError:
        print("Invalid Number!!!")

    # check if the space in the board is empty
    try:
        if board[choiceX] == " ":
            # putting the user's input into the board
            board[choiceX] = 'X'
        else:
            print()
            print("                     Sorry, that space is not empty!")
            time.sleep(1)
    except IndexError:
        print("Invalid Number!!!")
    except ValueError:
        print("Invalid Number!!!")
    except NameError:
        print("Invalid Number!!!")

    # check if X wins in 8 possibilities
    if is_winner(board, "X"):
        os.system('clear')
        print_board()
        print()
        print('                     X wins! Congratulations')
        break

    os.system('clear')
    game_instructions()
    print_board()

    # check for a tie
    if is_board_full(board):
        print()
        print('                     You Tie!                ')
        break

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Player O
    # getting user input
    global choiceO
    try:
        choiceO = int(input("Please choose an empty space for O."))
    except IndexError:
        print("Invalid Number!!!")
    except ValueError:
        print("Invalid Number!!!")
    except NameError:
        print("Invalid Number!!!")

    # check if the space in the board is empty
    try:
        if board[choiceO] == " ":
            # putting the user's input into the board
            board[choiceO] = 'O'
        else:
            print("Sorry, that space is not empty!")
            time.sleep(1)
    except IndexError:
        print("Invalid Number!!!")
    except ValueError:
        print("Invalid Number!!!")
    except NameError:
        print("Invalid Number!!!")

    # check for O win in 8 possibilities
    if is_winner(board, "O"):
        os.system('clear')
        print_board()
        print('                     O wins! Congratulations')
        break

    # check for a tie
    if is_board_full(board):
        print('                     You Tie!')
        break
