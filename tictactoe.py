#!/usr/local/bin/python

"""
Importing external modules
"""
# We'll need to know which OS we are running on
from sys import platform
# We will want to clear the screen from time to time
from os import system

"""
Declaring Global Variables
"""
# Dictionary containing the board with the players' moves
scoreboard = {'r1': {'c1': ' ', 'c2': ' ','c3': ' '},
              'r2': {'c1': ' ', 'c2': ' ','c3': ' '},
              'r3': {'c1': ' ', 'c2': ' ','c3': ' '}}
## Dictionary containing the board's template, to allow players
#+  to choose their next move
board_template = {'r1': {'c1': 'a', 'c2': 'b','c3': 'c'},
                  'r2': {'c1': 'd', 'c2': 'e','c3': 'f'},
                  'r3': {'c1': 'g', 'c2': 'h','c3': 'i'}}
# Players' names - player1 is always 'X' and always starts
player1 = ''
player2 = ''
# A global var to capture the OS we are running on, just in case
op_sys = ''
## What is the correct command to clear the screen? Let's capture
#+  it in a global var..
clr_comm = ''
active_player = ''
game_over = False


"""
Defining functions
"""
def print_header():
    """
    This function prints the "header" for the game: things like the
    players' names, etc.
    This should be printed every time the board is displayed, but not
    before players pick their names, etc.
    """
    pass


def clear_screen():
    """
    This function clears the screen.
    We capture what system (Windows, Linux, OS X) the game is running
    on in a global var with the init_game() function. We also set in the
    same function the correct command to clear the screen.
    This should be called after every move (if the move is valid), before
    the board is updated and printed out again.
    """
    dummy_var = system(clr_comm)
    pass


def print_odd_line(board,row):
    """
    This function prints an odd line, which contains both fixed values and
    players' pieces (or empty cells).
    It takes 2 parameters: the name of the array to get the values from
    (actual players' moves, or board template) and the key identifying the
    actual row to display the values for (this could be 'r1', 'r2' or 'r3').
    """
    #global scoreboard
    print '\t\t'+board[row]['c1']+'|'+board[row]['c2']+'|'+board[row]['c3']


def print_even_line():
    """
    This function prints an even line, which is constant and has no players'
    pieces.
    It does not need any input, output is always the same.
    """
    print "\t\t-+-+-"


def print_board(board):
    """
    Generic function that prints a board - this could be the actual playing
    board, or the board template.
    It takes one parameter (a dictionary containing the values to be displayed).
    It relies on 2 functions to print odd lines (containing the actual players'
    moves) and even lines (decorations).
    """
    print_odd_line(board,'r1')
    print_even_line()
    print_odd_line(board,'r2')
    print_even_line()
    print_odd_line(board,'r3')


def update_line(pos,value):
    """
    This function updates the values in the dictionary:
    - it takes 2 parameters:
    -- position: the position on the board that needs updating
    -- value: the value that needs to be recorded in the defined position (which
       depends on the player who just made their move)
    - it checks whether the chosen position is already occupied, in which case
      the function should exit with some error code
    -- the error code should be captured by the calling function which should
       print on screen and request that the same player makes another move
    """
    pass


def ask_player_name(num):
    """
    This function will be called (twice?) during the game's init phase.
    It is supposed to take one parameter (to identify which player it's taking
    the name of), ask the player's name and return it.

    ToDo: We could ask confirmation that the name entered is correct, and if not
    offer the player to reset their name - left for future improvement, keeping it
    simple for now.
    """
    print "\n\tHello Player #%s" % (num)

    if num == 1:
        # We need to read the player's name from console
        player_name = raw_input("\n\tYou will start the game and use X's"
                                " - What is your name? [Press Enter to confirm]\n\n\t")
    else:
        player_name = raw_input("\n\tYou will go second and use O's"
                                " - What is your name? [Press Enter to confirm]\n\n\t")

    return player_name


def is_choice_valid(choice):
    """
    This function checks the player's choice against the board template dictionary.
    If the choice is still in the dictionary, then it's valid and the function returns
    True. Otherwise the function returns False.
    """
    # Create a list with all values in board template
    l = []
    for r in ['r1', 'r2', 'r3']:
        for c in ['c1', 'c2', 'c3']:
            l.append(board_template[r][c])

    # Remove duplicates (eg. blanks), and then remove blank (if present)
    l = set(l)
    if ' ' in l:
        l.remove(' ')

    # Return True if choice is valid, False if it is not
    if choice in l:
        return True
    else:
        return False


def ask_for_choice():
    """
    This function asks the active player for their choice, and returns it.
    Before returning the player's choice, it validates that it is a valid one:
    - is the selected letter one of the available ones?
    """
    repeat_loop = True
    clear_screen()

    while repeat_loop == True:
        print "\n\t" + active_player + " make your move!\n"
        print "\n\tThis is the board:\n"
        print_board(scoreboard)
        print "\n\tSelect one of the boxes from the template below\n"
        print_board(board_template)
        choice = raw_input("\n\tYour move [letter + Enter to confirm]: ")

        if is_choice_valid(choice):
            repeat_loop = False
        else:
            clear_screen()
            print "\n\tYour choice ["+choice+"] is not valid!\n\t" \
                  "Please make a valid choice."

    return choice


def record_choice(choice):
    """
    This function is taking a player's choice and:
    a) recording it in the scoreboard dictionary
    b) take the corresponding letter out of the board template dictionary
    """
    # We need to make changes to the 2 boards
    global scoreboard
    global board_template
    # We also need to change the active player's name
    global active_player

    # Establishing which sign we need to use in the scoreboard
    if active_player == player1:
        sign = 'X'
    elif active_player == player2:
        sign = 'O'
    else:
        clear_screen()
        print "\n\tWho is playing?"
        exit(100)

    # Determining which row and which column were selected by the player
    for r in ['r1', 'r2', 'r3']:
        for c in ['c1', 'c2', 'c3']:
            if choice == board_template[r][c]:
                row = r
                col = c

    # Debug - this could be used later on to confirm the player's choice
    # print "Row = "+row+"\nCol = "+col

    # Recording the player's move in the scoreboard
    scoreboard[row][col] = sign

    # Removing the option from the template
    board_template[row][col] = ' '

    # Debug
    # dummy_var = raw_input("")

    if not is_game_over():
        if active_player == player1:
            active_player = player2
        else:
            active_player = player1


def is_winning_combo(list):
    """
    This function takes a list as a parameter (the list contains 3
    objects itself, each object is a list of 2 strings).

    The function then checks in the scoreboard dictionary if the 3
    positions references by the parameter all contain the same sign
    (either 'X' or 'O').

    Function returns True if all 3 values are the same, False if they
    are not.
    """
    pass

def is_game_over():
    """
    This function checks in the template if there are any available choices,
    and then it checks in the scoreboard if there are 3 signs in a row.

    In case of no 3 signs in a row and choices still available, it returns
    False (the calling function will swap the active player).

    In case the game is over, it prints the result on the screen and exits
    from the script entirely.
    """
    ## First of all we check if all possible moves have always been made.
    #+ This means that all choices have been eliminated from the template.
    l = []
    for r in ['r1', 'r2', 'r3']:
        for c in ['c1', 'c2', 'c3']:
            l.append(board_template[r][c])

    # Removing duplicates (eg. blanks), and then remove blank (if present)
    l = set(l)
    if ' ' in l:
        l.remove(' ')
    if len(l) == 0:
        clear_screen()
        print "\n\tThe game is over!\n\n" \
              "\tThis is a 'cat' game (stalemate) and there is no winner!\n\n" \
              "\tThis is the final board:\n"
        print_board(scoreboard)
        print "\n"
        exit(0)

    # Checking if the active player achieved 3 in a row
    # This is a dictionary with the list of possible combinations
    combo = {'c1': [['r1', 'c1'], ['r1', 'c2'], ['r1', 'c3']],
             'c2': [['r2', 'c1'], ['r2', 'c2'], ['r2', 'c3']],
             'c3': [['r3', 'c1'], ['r3', 'c2'], ['r3', 'c3']],
             'c4': [['r1', 'c1'], ['r2', 'c1'], ['r3', 'c1']],
             'c5': [['r1', 'c2'], ['r2', 'c2'], ['r3', 'c2']],
             'c6': [['r1', 'c3'], ['r2', 'c3'], ['r3', 'c3']],
             'c7': [['r1', 'c1'], ['r2', 'c2'], ['r3', 'c3']],
             'c8': [['r3', 'c1'], ['r2', 'c2'], ['r1', 'c3']]}

    ## If the game is not over, we return false so that the calling function
    #+ can swap the active player's name
    return False
    pass


def init_game():
    """
    This function is called at the beginning of the game and is required to set
    up the game itself:
    - Print out the rules of the game
    - Ask and assign names to Player 1 and Player 2
    - Other?
    """
    
    # Declaring global vars
    global op_sys
    global clr_comm
    global player1
    global player2
    global active_player
    
    # Let's see which OS we are running on:
    op_sys = platform
    
    # Let's set the correct command to clear the screen
    if op_sys == 'darwin':
        clr_comm = 'clear'
    else:
        clr_comm = 'not set'

    # Let's print out the rules of the game
    clear_screen()
    print "\n\tHello Players, welcome to Tic Tac Toe! These are the rules:\n"
    print "\tThe object of Tic Tac Toe is to get three in a row." \
          "\n\tYou play on a three by three game board." \
          "\n\tThe first player is known as X and the second is O." \
          "\n\tPlayers alternate placing Xs and Os on the game board until either" \
          "\n\topponent has three in a row or all nine squares are filled.\n"
    dummy_var = raw_input("\n\tPress Enter to set up the game: ")


    # Let's set up the players' names
    clear_screen()
    player1 = ask_player_name(1)
    if player1 == '':
        player1 = "Player X"
    clear_screen()
    player2 = ask_player_name(2)
    if player2 == '':
        player2 = "Player O"

    # Let's set the active player var
    active_player = player1

    # Lets's greet the players and recap their names and playing order
    clear_screen()
    print "\n\tHello players, these are the names you selected:\n"
    print "\tPlayer1: %s" % player1
    print "\tPlayer2: %s" % player2
    print "\n\t'%s' will go first and use X's, while '%s' will go second" \
          " and use O's\n" % (player1,player2)
    dummy_var = raw_input("\n\tPress Enter to start the game: ")

    pass


def main():
    """
    This is the main body of the script.

    ToDo: it would be nice if we asked a player to confirm their move,
          and give them a chance to change it...
    """

    ## We define "game_over" as global because we use it to break out of the
    #+ main loop when we reach an exit condition
    global game_over

    ## We set up a loop to: a) ask for a player's choice (this also checks if
    #+ the move is valid), record their move in the scoreboard dictionary, check
    #+ if the game is over
    while game_over == False:
        # Asking currently active user for their next move
        move = ask_for_choice()

        # Debug
        """
        if move == 'a':
            game_over = True
        """

        # Recording the last move in the scoreboard dictionary
        record_choice(move)

        # Checking if the game is over, and if there is a winner
        # is_game_over()

    ## When the game is over, we should print out the board and the name of
    #+ the winner

    print "\n\n\tThe game is over!\n"
    pass


## ---- ---- ----


init_game()

main()