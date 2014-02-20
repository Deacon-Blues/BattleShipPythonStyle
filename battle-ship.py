__author__ = 'Deacon-Blues'

import random
# Dictionary, column letter as value, column number as key
column_letter = {'A': 1,
                 'B': 2,
                 'C': 3,
                 'D': 4,
                 'E': 5}

# First item is column second item is row
ship = []

board = []  # Empty list to be populated by fill_board function

x = ['1', '2', '3', '4', '5']  # List of row numbers, inserted into the front of each row later on

y = [" ", 'A', 'B', 'C', 'D', 'E']  # Needs space to properly print in 5x5 grid


# Function responsible for creating 5 lists of 5 O's
def fill_board():
    for i in range(0, 5):
        board.append(['O'] * 5)  # Adds 5 lists of 5 'O's to board list
    fill_grid()


# Function responsible for inserting 1-5 at the front of each list
def fill_grid():
    for row in board:  # For every row of O's
        row.insert(0, x.pop(0))  # Insert the first number from the x list at the front


# Function responsible for printing board list as a 5x5 grid
def print_board():
    print(" ".join(y))
    for row in board:
        print(" ".join(row))


# Do not need 2 random number functions
def random_row():
    random.randrange(1, 6)


# But will if change board dimensions
def random_column():
    random.randrange(1, 6)


# Function that takes random number functions as coordinates
def hide_ship():
    ship.append(random_column())  # sets first item in ship to column
    ship.append(random_row())  # sets second item in ship to row


# Function responsible for replacing 'O's with 'X's upon missing
# Takes list as input
def miss(target):
    column = target[0]  # Column = First element of target lst
    row = (target[1] - 1)  # Row = Second element of target lst - 1( -1 makes it work correctly, not sure why)
    missed_target = [column, row]  # Consider slimming this function down
    board_index = missed_target[0]  # As a lot of this is not needed
    board_list = missed_target[1]  # Written like this to help understand what represented what
    board[board_list][board_index] = "X"  # In relation to the board
    print_board()


# Function responsible for checking if target(list) has already been tried
def check_if_tried(target):
    board_index = target[0]  # Board index(aka column) = 1st element in target list
    board_row = target[1] - 1  # Board row(aka list) = 2nd element in target list
    if board[board_row][board_index] == "X":  # If target list coordinates(column and row) are already X
        return True  # Return true because X means its already been tried
    else:  # else
        return False  # False because it has not been tried


# Function that gathers user input and assigns it as elements in a list(named target)
def get_target():
        target = []  # Target list
        coordinates = input('Where would you like to fire sir?: ')  # Sets coordinate var to user input(letter-number)
        column = coordinates[0].upper()  # First character in coordinates string = column
        row = coordinates[1]  # Second character in coordinates string = row
        column = column_letter[column.upper()]  # Sets user input letter to equivalent dictionary key
        row = int(row)  # Sets row to int form
        target.append(column)  # Adds column to target list
        target.append(row)  # Add row to target list
        return target  


# Function that takes user inputted coordinates and checks for hit or miss
def shoot():
    turn = 0  # Sets turn var to 0
    running = True
    while running:  # While turn < 10
        target = get_target()
        if check_if_tried(target) is False:
            if target == ship:  # If target list == ship list
                running = False  # Sets turn var to 10 as to end function
                print('Hit! You win!')  # You dun won!
            else:  # Else
                miss(target)  # Run miss function on target list
                turn += 1  # add 1 to turn var
                print('Miss! You have tried', turn, 'times!')
        else:
            print('You already tried that!')
    print('You loose!')


def main():
    fill_board()
    print_board()
    hide_ship()
    shoot()
main()