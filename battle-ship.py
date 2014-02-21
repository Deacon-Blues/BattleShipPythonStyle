__author__ = 'Deacon-Blues'

import random
import time

# Dictionary, column letter as value, column number as key
column_letter = {1: 'A',
                 2: 'B',
                 3: 'C',
                 4: 'D',
                 5: 'E',
                 6: 'F',
                 7: 'G',
                 8: 'H'}

column_number = {'A': 1,
                 'B': 2,
                 'C': 3,
                 'D': 4,
                 'E': 5,
                 'F': 6,
                 'G': 7,
                 'H': 8}

x = []  # List of row numbers, inserted into the front of each row later on

columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

rows = [1, 2, 3, 4, 5, 6, 7, 8]

# First item is column second item is row
ship_origin = []

ship = []

board = []  # Empty list to be populated by fill_board function

y = [" ", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # Needs space to properly print in 8x8 grid

port = []  # Empty list, will represent ship origin coordinates + 1

starboard = []  # Empty list, will represent ship origin coordinates - 1


# Function responsible for creating 8 lists of 8 O's
def fill_board():
    for i in range(0, 8):
        board.append(['O'] * 8)  # Adds 8 lists of 8 'O's to board list


# Refills x list with numbers 1-8 in string form
def fill_x(lst):
    for number in range(1, 9):
        lst.append(str(number))


# Function responsible for inserting 1-8 at the front of each list
def fill_grid():
    fill_x(x)
    for row, i in zip(board, x):  # Used Zip function to loop through 2 separate lists
        row.insert(0, str(i))  # Insert the first number from the x list at the front


# Function responsible for printing board list as a 8x8 grid
def print_board():
    print(" ".join(y))
    for row in board:
        print(" ".join(row))


def random_column_key():
    return random.randrange(2, 8)


# Converts column values to their int counterparts
def convert_column():
    ship_origin[0] = column_letter[ship_origin[0]]
    port[0] = column_letter[port[0]]
    starboard[0] = column_letter[starboard[0]]


# Function that takes random number functions as coordinates
def hide_ship():
    direction = random.randrange(1, 3)
    if direction == 1:
        ship_origin.append(random_column_key())  # sets first item in ship to column
        ship_origin.append(random.randrange(2, 8))  # sets second item in ship to row
        port.append(ship_origin[0])  # Adds origin column to port list
        port.append(ship_origin[1] + 1)  # Adds origin row + 1 to port list
        starboard.append(ship_origin[0])  # Adds origin column to starboard list
        starboard.append(ship_origin[1] - 1)  # Adds origin row - 1 to starboard list
        convert_column()
        ship.append(ship_origin)  # Adds origin coordinates to ship list
        ship.append(port)  # Adds port coordinates to ship list
        ship.append(starboard)  # Adds starboard coordinates to ship list
    else:
        ship_origin.append(random_column_key())  # sets first item in ship to column
        ship_origin.append(random.randrange(2, 8))  # sets second item in ship to row
        port.append(ship_origin[0] + 1)  # Adds origin column + 1 to port list
        port.append(ship_origin[1])  # Adds origin row to port list
        starboard.append(ship_origin[0] - 1)  # Adds origin column - 1 to starboard list
        starboard.append(ship_origin[1])  # Adds origin row to starboard list
        convert_column()
        ship.append(ship_origin)  # Adds origin coordinates to ship list
        ship.append(port)  # Adds port coordinates to ship list
        ship.append(starboard)  # Adds starboard coordinates to ship list


# Function responsible for replacing 'O's with 'X's upon missing
# Takes list as input
def miss(target):
    column = column_number[target[0].upper()]  # Column = 1st element's value:key in column_number Dictionary
    row = (target[1] - 1)  # Row = Second element of target lst - 1( -1 makes it work correctly, not sure why)
    missed_target = [column, row]  # Consider slimming this function down
    board_index = missed_target[0]  # As a lot of this is not needed
    board_list = missed_target[1]  # Written like this to help understand what represented what
    board[board_list][board_index] = "X"  # In relation to the board
    print_board()


# Function responsible for replacing 'O's with '$'s upon hitting
# Takes target list as input [column, row]
def hit(target):
    column = column_number[target[0].upper()]  # Column = 1st element's value:key in column_number Dictionary
    row = (target[1] - 1)  # Row = Second element of target lst - 1( -1 makes it work correctly, not sure why)
    missed_target = [column, row]  # Consider slimming this function down
    board_index = missed_target[0]  # As a lot of this is not needed
    board_list = missed_target[1]  # Written like this to help understand what represented what
    board[board_list][board_index] = "$"  # In relation to the board
    print_board()


# Function responsible for checking if target(list) has already been tried
def check_if_tried(target):
    board_index = column_number[target[0].upper()]  # Board index(aka column) = 1st element's value:key in column_number
    board_row = target[1] - 1  # Board row(aka list) = 2nd element in target list
    if board[board_row][board_index] == "X" or board[board_row][board_index] == '$':
        return True  # Return true because X means its already been tried
    else:  # else
        return False  # False because it has not been tried


# Function that gathers user input and assigns it as elements in a list(named target)
def get_target():
        target = []  # Target list
        running = True
        while running:
            coordinates = input('Where would you like to fire sir?: ')  # Sets coordinate var to user input
            if check_if_cheat(coordinates) is False:  # If input is not cheat code
                column = coordinates[0].upper()  # First character in coordinates string = column
                row = coordinates[1]  # Second character in coordinates string = row
                row = int(row)  # Sets row to int form
                target.append(column)  # Adds column to target list
                target.append(row)  # Add row to target list
                return target


# Checks if column input is valid
def valid_column(target):
    if target[0].upper() in columns:
        return True
    else:
        return False


# Checks if row input is valid
def valid_row(target):
    if target[1] in rows:
        return True
    else:
        return False


# Checks if user inputs cheat code
def check_if_cheat(coordinates):
    if coordinates == 'fs':
        print(ship)
        return True
    else:
        return False


# Function that gathers input on rather user wishes to continue playing
def play_again():
    print('Would You like to play again?')
    go_again = input('Type \'EXIT\' to quit, or press ENTER to play again:  ')
    return go_again


# Function that takes user inputted coordinates and checks for hit or miss
def shoot():
    turn = 0  # Sets turn var to 0
    running = True
    while running:  # While running is True
        target = get_target()
        if valid_column(target) is True and valid_row(target) is True:
            if check_if_tried(target) is False:
                turn += 1  # add 1 to turn var
                if target in ship:  # If target list == ship list
                    ship.remove(target)
                    if not ship:
                        running = False  # Sets turn var to 10 as to end function
                        print('---BOOM HEADSHOT, YOU SANK HIS BRAP SHIP!---')  # You dun won!
                    else:
                        hit(target)
                        print('Hit!')
                else:  # Else
                    miss(target)  # Run miss function on target list
                    print('Miss! You have tried', turn, 'times!')
            else:
                print('We\'ve already bombarded that location sir!')
        elif valid_column(target) is False and valid_row(target) is True:  # This logic
            print('Invalid Column input!')
        elif valid_column(target) is True and valid_row(target) is False:  # handles invalid inputs
            print('Invalid row input!')
        elif valid_column(target) is False and valid_row(target) is False:  # for column, row, and both column and row
            print('Invalid inputs!')
        else:
            print('Error')
    return turn


# Clears  a given list and returns it
def clear_lst(lst):
    lst.clear()
    return lst


def main():
    running = True
    while running:
        clear_lst(board)  # Change all instances of clear_lst to one function at a later date
        clear_lst(ship)
        clear_lst(ship_origin)
        clear_lst(port)
        clear_lst(starboard)
        fill_board()
        fill_grid()
        print_board()
        hide_ship()
        print('It took you', shoot(), 'Turns to win!')
        if play_again() == "":
            print('The Game will restart in 10 seconds')
            timer = 10
            while timer > 0:
                time.sleep(1)
                print(timer)
                timer -= 1
            running = True
        elif play_again() == "EXIT":
            running = False
main()