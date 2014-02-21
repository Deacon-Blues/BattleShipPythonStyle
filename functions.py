__author__ = 'Deacon-Blues'

import random


# Function responsible for creating 5 lists of 5 O's
def fill_board():
    for i in range(0, 5):
        board.append(['O'] * 5)  # Adds 5 lists of 5 'O's to board list
    fill_grid()


# Function responsible for inserting 1-5 at the front of each list
def fill_grid():
    for row in board:  # For every row of O's
        row.insert(0, x.pop(0))  # Insert the first number from the x list at the front


# Refills x list with numbers 1-5 in string form
def fill_x():
    for number in range(1, 6):
        x.append(str(number))


# Function responsible for printing board list as a 5x5 grid
def print_board():
    print(" ".join(y))
    for row in board:
        print(" ".join(row))


def random_column_key():
    return column_letter[random.randrange(2, 5)]


# Function that takes random number functions as coordinates
def hide_ship():
    ship_origin.append(random_column_key())  # sets first item in ship to column
    ship_origin.append(random.randrange(1, 6))  # sets second item in ship to row
    port = []  # Empty list, will represent ship origin coordinates + 1
    starboard = []  # Empty list, will represent ship origin coordinates - 1
    port.append(ship_origin[0])  # Adds origin column to port list
    port.append(ship_origin[1] + 1)  # Adds origin row + 1 to port list
    starboard.append(ship_origin[0])  # Adds origin column to starboard list
    starboard.append(ship_origin[1] - 1)  # Adds origin row + 1 to starboard list
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
    if board[board_row][board_index] == "X" or '$':  # If target list coordinates(column and row) are already X
        return True  # Return true because X means its already been tried
    else:  # else
        return False  # False because it has not been tried


# Function that gathers user input and assigns it as elements in a list(named target)
def get_target():
        target = []  # Target list
        coordinates = input('Where would you like to fire sir?: ')  # Sets coordinate var to user input(letter-number)
        column = coordinates[0].upper()  # First character in coordinates string = column
        row = coordinates[1]  # Second character in coordinates string = row
        row = int(row)  # Sets row to int form
        target.append(column)  # Adds column to target list
        target.append(row)  # Add row to target list
        return target


# Checks if column input is valid
def valid_column(target):
    if target[0] in y:
        return True
    else:
        return False


# Checks if row input is valid
def valid_row(target):
    if target[1] in range(1, 6):
        return True
    else:
        return False


# Function that takes user inputted coordinates and checks for hit or miss
def shoot():
    turn = 0  # Sets turn var to 0
    running = True
    while running:  # While running is True
        target = get_target()
        if valid_column(target) is True and valid_row(target) is True:
            if check_if_tried(target) is False:
                if target in ship:  # If target list == ship list
                    ship.remove(target)
                    if not ship:
                        running = False  # Sets turn var to 10 as to end function
                        print('Hit! You sank his Battle Ship! You win!')  # You dun won!
                    else:
                        hit(target)
                        print('Hit!')
                else:  # Else
                    miss(target)  # Run miss function on target list
                    turn += 1  # add 1 to turn var
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


def main():
    fill_board()
    print_board()
    hide_ship()
    print(ship)
    shoot()


