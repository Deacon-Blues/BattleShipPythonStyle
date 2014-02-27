__author__ = 'Terrance'

import random
import time
import copy


# Clears a given list and returns it
def clear_lst(lst):
    lst.clear()
    return lst


# Runs clear_list function on all(or at least all currently known) lists that will not break the program.
def clear_lists():
    clear_lst(ships)
    clear_lst(bird_of_prey)
    clear_lst(war_bird)
    clear_lst(borg_cube)
    clear_lst(ship_1_damage)
    clear_lst(ship_2_damage)
    clear_lst(ship_3_damage)
    clear_lst(myships)
    clear_lst(defiant)
    clear_lst(voyager)
    clear_lst(enterprise)
    clear_lst(next_targets)


# Creates a list of 8 lists each consisting of 8 'O's
# Takes a given board as input. Used to create player and enemy board
def fill_board(some_board):
    for i in range(0, 8):
        some_board.append(['O'] * 8)  # Adds 8 lists of 8 'O's to board list


# Refills x list with numbers 1-8 in string form
def fill_x(lst):
    for number in range(1, 9):
        lst.append(str(number))


# Inserts a number 1-8 to the front of list 0-7 in a given board.
# Gives the game board its row labels
def fill_grid(some_board):
    fill_x(x)
    for row, i in zip(some_board, x):  # Used Zip function to loop through 2 separate lists
        row.insert(0, str(i))  # Insert the first number from the x list at the front


# Clears both boards(The list of lists)
# Runs the fill_board and fill_grid function on both boards
def fill_boards():
    clear_lst(myboard)  # Clear global myboard list
    clear_lst(board)  # Clear global board list
    fill_board(board)  # populates board list with appropriate number of O's
    fill_grid(board)  # adds the row labels to board list
    fill_board(myboard)  # populates myboard list with appropriate number of O's
    fill_grid(myboard)  # adds row labels to myboard list


# Prints two game boards in a 8 x 8 grid
# Separates the game boards by a tab(4 spaces)
# Adds the column tags to the top of the board
# Joins each list item by a vertical dash( | )
def print_board():
    print(" | ".join(y), '\t', " | ".join(y))
    print('---------------------------------', '\t', '----------------------------------')
    for row, row_again in zip(board, myboard):
        print(" | ".join(row), '\t', " | ".join(row_again))
        print('---------------------------------', '\t', '----------------------------------')


# Converts column values to their int counterparts
# Uses dictionaries to convert between the two
def convert_column(*args):
    args[0][0] = column_letter[args[0][0]]
    args[1][0] = column_letter[args[1][0]]
    try:
        args[2][0] = column_letter[args[2][0]]

    except IndexError:
        pass
    try:
        args[3][0] = column_letter[args[3][0]]
    except IndexError:
        pass


# Function that takes random number functions as coordinates
def hide_ship(ship):
    port = []  # Empty list, will represent ship origin coordinates + 1
    starboard = []  # Empty list, will represent ship origin coordinates - 1
    ship_origin = []  # Ship starting location
    starboard_again = []
    direction = random.randrange(1, 3)
    if ship is war_bird:
        if direction == 1:
            ship_origin.append(random.randrange(2, 8))  # sets first item in ship to random number 2-7
            ship_origin.append(random.randrange(2, 8))  # sets second item in ship to random number 2-7
            port.append(ship_origin[0])  # Adds origin column to port list
            port.append(ship_origin[1] + 1)  # Adds origin row + 1 to port list
            starboard.append(ship_origin[0])  # Adds origin column to starboard list
            starboard.append(ship_origin[1] - 1)  # Adds origin row - 1 to starboard list
            convert_column(ship_origin, port, starboard)  # Converts the column(first) value of each list to its Letter
            ship.append(ship_origin)  # Adds origin coordinates to ship list
            ship.append(port)  # Adds port coordinates to ship list
            ship.append(starboard)  # Adds starboard coordinates to ship list
        else:
            ship_origin.append(random.randrange(2, 8))  # sets first item in ship to random number 2-7
            ship_origin.append(random.randrange(2, 8))  # sets first item in ship to random number 2-7
            port.append(ship_origin[0] + 1)  # Adds origin column + 1 to port list
            port.append(ship_origin[1])  # Adds origin row to port list
            starboard.append(ship_origin[0] - 1)  # Adds origin column - 1 to starboard list
            starboard.append(ship_origin[1])  # Adds origin row to starboard list
            convert_column(ship_origin, port, starboard)  # Converts the column(first) value of each list to its Letter
            ship.append(ship_origin)  # Adds origin coordinates to ship list
            ship.append(port)  # Adds port coordinates to ship list
            ship.append(starboard)  # Adds starboard coordinates to ship list
    elif ship is bird_of_prey:
        if direction == 1:
            ship_origin.append(random.randrange(1, 8))  # sets first item in ship to random number 2-7
            ship_origin.append(random.randrange(1, 8))  # sets second item in ship to random number 2-7
            port.append(ship_origin[0])  # Adds origin column to port list
            port.append(ship_origin[1] + 1)  # Adds origin row + 1 to port list
            convert_column(ship_origin, port)  # Converts the column(first) value of each list to its Letter
            ship.append(ship_origin)  # Adds origin coordinates to ship list
            ship.append(port)  # Adds port coordinates to ship list
        else:
            ship_origin.append(random.randrange(1, 8))  # sets first item in ship to random number 2-7
            ship_origin.append(random.randrange(1, 8))  # sets first item in ship to random number 2-7
            port.append(ship_origin[0] + 1)  # Adds origin column + 1 to port list
            port.append(ship_origin[1])  # Adds origin row to port list
            convert_column(ship_origin, port)  # Converts the column(first) value of each list to its Letter
            ship.append(ship_origin)  # Adds origin coordinates to ship list
            ship.append(port)  # Adds port coordinates to ship list
    elif ship is borg_cube:
        ship_origin.append(random.randrange(1, 8))  # sets first item in ship to random number 2-7
        ship_origin.append(random.randrange(1, 8))  # sets second item in ship to random number 2-7
        port.append(ship_origin[0] + 1)  # Adds origin column to port list
        port.append(ship_origin[1])  # Adds origin row + 1 to port list
        starboard.append(ship_origin[0])  # Adds origin column to starboard list
        starboard.append(ship_origin[1] + 1)  # Adds origin row - 1 to starboard list
        starboard_again.append(port[0])
        starboard_again.append(port[1] + 1)
        convert_column(ship_origin, port, starboard, starboard_again)
        ship.append(ship_origin)  # Adds origin coordinates to ship list
        ship.append(port)  # Adds port coordinates to ship list
        ship.append(starboard_again)  # Adds starboard coordinates to ship list
        ship.append(starboard)


def hide_ships(one, two, three):
        hide_ship(one)  # Randomizes and checks coordinates for ship_1 list
        hide_ship(two)  # Randomizes and checks coordinates for ship_2 list
        hide_ship(three)  # Randomizes and checks coordinates for ship_3 list


# Takes User inputted coordinate runs various checks
# And If everything is in order convert the coord into numerical values in relation to the board
# Then add new set of coordinates to a given list(staging_ground) and will later be used to represent the ship_origin
def get_ship_origin(staging_ground):
    running = True
    while running:
        ship_origin = input('Enter Ship origin: ')
        column = column_number[ship_origin[0].upper()]
        row = ship_origin[1]
        try:
            row = int(row)
        except ValueError:
            print('Second character input should be a number 1-8')
            running = True
            return running
        coord = [column, row]
        if coord == [1, 1] or coord == [1, 8] or coord == [8, 8] or coord == [8, 1]:
            print('You have boxed yourself into a corner. There is no room to expand your ship')
            running = True
        else:
            if coord[0] in rows and coord[1] in rows:
                if check_if_already_occupied(coord) is False:
                    #board_index = column  # As a lot of this is not needed
                    #board_list = row - 1  # Written like this to help understand what represented what
                    #myboard[board_list][board_index] = '@'
                    staging_ground.append(coord)
                    running = False
                else:
                    running = True
            else:
                print('Invalid input1')
                running = True


# Extends ship one space to the north and one to the south of ship_origin
def extend_ship_vertical(staging_ground, a_ship):
    port = []
    port_again = []
    starboard = []
    starboard_again = []
    staging_ground_clone = copy.deepcopy(staging_ground)
    if a_ship is voyager:
        staging_ground_clone[0][1] += 1  # Adds one to the row value of ship_origin / Main_staging_ground
        port.append(staging_ground_clone[0][0])  # Adds new staging ground values
        port.append(staging_ground_clone[0][1])  # To port, to represent going down 1 row
        # Subtracts 2 from row value of ship_origin / staging_ground
        # This restores its original value - 1
        staging_ground_clone[0][1] -= 2
        starboard.append(staging_ground_clone[0][0])  # Adds new staging ground value
        starboard.append(staging_ground_clone[0][1])  # To starboard, to represent going up 1 row
        staging_ground.append(port)  # Adds new port and starboard lists(containing extended coordinates of ship origin)
        staging_ground.append(starboard)  # To the original list of lists containing the ship_origin coordinates
    elif a_ship is defiant:
        staging_ground_clone[0][1] += 1  # Adds one to the column value of ship_origin / Main_staging_ground
        port.append(staging_ground_clone[0][0])   # Adds new staging ground values
        port.append(staging_ground_clone[0][1])  # To starboard, to represent going to the right one column
        staging_ground.append(port)  # Adds new port and starboard lists(containing extended coordinates of ship origin)
    elif a_ship is enterprise:
        staging_ground_clone[0][1] += 1  # Adds one to the row value of ship_origin / Main_staging_ground
        port.append(staging_ground_clone[0][0])  # Adds new staging ground values
        port.append(staging_ground_clone[0][1])  # To port, to represent going down 1 row
        staging_ground_clone[0][1] += 1  # Adds one to the row value of ship_origin / Main_staging_ground
        port_again.append(staging_ground_clone[0][0])  # Adds new staging ground values
        port_again.append(staging_ground_clone[0][1])  # To port, to represent going down 1 row
        # Subtracts 2 from row value of ship_origin / staging_ground
        # This restores its original value - 1
        staging_ground_clone[0][1] -= 3
        starboard.append(staging_ground_clone[0][0])  # Adds new staging ground value
        starboard.append(staging_ground_clone[0][1])  # To starboard, to represent going up 1 row
        staging_ground_clone[0][1] -= 1
        starboard_again.append(staging_ground_clone[0][0])  # Adds new staging ground value
        starboard_again.append(staging_ground_clone[0][1])  # To starboard, to represent going up 1 row
        staging_ground.append(port)  # Adds new port and starboard lists(containing extended coordinates of ship origin)
        staging_ground.append(starboard)  # To the original list of lists containing the ship_origin coordinates
        staging_ground.append(port_again)
        staging_ground.append(starboard_again)


# Extends ship one space to the east and one space to the west
def extend_ship_horizontal(staging_ground, a_ship):
    port = []
    port_again = []
    starboard = []
    starboard_again = []
    staging_ground_clone = copy.deepcopy(staging_ground)
    if a_ship is voyager:
        staging_ground_clone[0][0] += 1  # Adds one to the column value of ship_origin / Main_staging_ground
        port.append(staging_ground_clone[0][0])   # Adds new staging ground values
        port.append(staging_ground_clone[0][1])  # To starboard, to represent going to the right one column
        # Subtracts 2 from column value of ship_origin / staging_ground
        # This restores its original value - 1
        staging_ground_clone[0][0] -= 2
        starboard.append(staging_ground_clone[0][0])  # Adds new staging ground value
        starboard.append(staging_ground_clone[0][1])  # To Starboard to represent going left one column
        staging_ground.append(port)  # Adds new port and starboard lists(containing extended coordinates of ship origin)
        staging_ground.append(starboard)  # To the original list of lists containing the ship_origin coordinates
    elif a_ship is defiant:
        staging_ground_clone[0][0] += 1  # Adds one to the column value of ship_origin / Main_staging_ground
        port.append(staging_ground_clone[0][0])   # Adds new staging ground values
        port.append(staging_ground_clone[0][1])  # To starboard, to represent going to the right one column
        staging_ground.append(port)  # Adds new port and starboard lists(containing extended coordinates of ship origin)
    elif a_ship is enterprise:
        staging_ground_clone[0][0] += 1  # Adds one to the row value of ship_origin / Main_staging_ground
        port.append(staging_ground_clone[0][0])  # Adds new staging ground values
        port.append(staging_ground_clone[0][1])  # To port, to represent going down 1 row
        staging_ground_clone[0][0] += 1  # Adds one to the row value of ship_origin / Main_staging_ground
        port_again.append(staging_ground_clone[0][0])  # Adds new staging ground values
        port_again.append(staging_ground_clone[0][1])  # To port, to represent going down 1 row
        # Subtracts 2 from row value of ship_origin / staging_ground
        # This restores its original value - 1
        staging_ground_clone[0][0] -= 3
        starboard.append(staging_ground_clone[0][0])  # Adds new staging ground value
        starboard.append(staging_ground_clone[0][1])  # To starboard, to represent going up 1 row
        staging_ground_clone[0][0] -= 1
        starboard_again.append(staging_ground_clone[0][0])  # Adds new staging ground value
        starboard_again.append(staging_ground_clone[0][1])  # To starboard, to represent going up 1 row
        staging_ground.append(port)  # Adds new port and starboard lists(containing extended coordinates of ship origin)
        staging_ground.append(starboard)  # To the original list of lists containing the ship_origin coordinates
        staging_ground.append(port_again)
        staging_ground.append(starboard_again)


# Uses get_ship_origin function to generate an unoccupied ship_origin coordinate
# Then uses conditional statements to determine if there is only one possible direction of expansion
# If so, expand ship that direction. If not, Let user choose direction to expand ship
# Adds Extended ship to a given ship list(myship_1(2)(3))
# Uses main_staging_ground coordinates to place ship on the board(Change all applicable coordinates to '*'s
# Prints the, now modified, board
def hide_myships(ship):
    global main_staging_ground
    getting_ship_origin = True
    while getting_ship_origin:
        main_staging_ground = []
        get_ship_origin(main_staging_ground)
        if main_staging_ground[0][0] == 1 or main_staging_ground[0][0] == 8:
            extend_ship_vertical(main_staging_ground, ship)
        elif main_staging_ground[0][1] == 1 or main_staging_ground[0][1] == 8:
            extend_ship_horizontal(main_staging_ground, ship)
        else:
            choosing_v_h = True
            while choosing_v_h:
                print('Would you like to place your ship [V]ertical or [H]orizontal: ')
                v_or_h = input('Enter: V for Vertical or H for horizontal: ')
                if v_or_h.upper() == 'V':
                    extend_ship_vertical(main_staging_ground, ship)
                    choosing_v_h = False
                elif v_or_h.upper() == 'H':
                    extend_ship_horizontal(main_staging_ground, ship)
                    choosing_v_h = False
                else:
                    print('Input Error')
                    choosing_v_h = True
        if ship is defiant:
            if myboard[main_staging_ground[0][1] - 1][main_staging_ground[0][0]] == '@':
                print('If you deploy there your ships will collide!')
                getting_ship_origin = True
            elif myboard[main_staging_ground[1][1] - 1][main_staging_ground[1][0]] == '@':
                print('If you deploy there your ships will collide!')
                getting_ship_origin = True
            else:
                getting_ship_origin = False
        elif ship is voyager:
            if myboard[main_staging_ground[0][1] - 1][main_staging_ground[0][0]] == '@':
                print('If you deploy there your ships will collide!')
                getting_ship_origin = True
            elif myboard[main_staging_ground[1][1] - 1][main_staging_ground[1][0]] == '@':
                print('If you deploy there your ships will collide!')
                getting_ship_origin = True
            elif myboard[main_staging_ground[2][1] - 1][main_staging_ground[2][0]] == '@':
                print('If you deploy there your ships will collide!')
                getting_ship_origin = True
            else:
                getting_ship_origin = False
        elif ship is enterprise:
            if myboard[main_staging_ground[0][1] - 1][main_staging_ground[0][0]] == '@':
                print('If you deploy there your ships will collide!')
                getting_ship_origin = True
            elif myboard[main_staging_ground[1][1] - 1][main_staging_ground[1][0]] == '@':
                print('If you deploy there your ships will collide!')
                getting_ship_origin = True
            elif myboard[main_staging_ground[2][1] - 1][main_staging_ground[2][0]] == '@':
                print('If you deploy there your ships will collide!')
                getting_ship_origin = True
            elif myboard[main_staging_ground[3][1] - 1][main_staging_ground[3][0]] == '@':
                print('If you deploy there your ships will collide!')
                getting_ship_origin = True
            elif myboard[main_staging_ground[4][1] - 1][main_staging_ground[4][0]] == '@':
                print('If you deploy there your ships will collide!')
                getting_ship_origin = True
            else:
                getting_ship_origin = False
    ship.append(main_staging_ground)
    print('-----------------------------SHIP DEPLOYED------------------------------')
    place_ship(main_staging_ground, myboard)
    print_board()


# Function that gathers user input and assigns it as elements in a list(named target)
def get_target():
        target = []  # Target list
        running = True
        while running:
            coordinates = input('Where would you like to open your orphan factory?: ')
            if check_if_cheat(coordinates) is False and len(coordinates) == 2:  # If input is not cheat code
                if coordinates[0].upper() in columns and int(coordinates[1]) in rows:  # If column and row input is ok
                    column = coordinates[0].upper()  # First character in coordinates string = column
                    row = coordinates[1]  # Second character in coordinates string = row
                    row = int(row)  # Sets row to int form
                    target.append(column)  # Adds column to target list
                    target.append(row)  # Add row to target list
                    return target
                else:  # Else if coordinates invalid
                    print('Input should include a letter A-E and a number 1-8')  # Error message
                    running = True  # Return to start of loop

            # If not cheat code, but length of input is not equal to two
            elif len(coordinates) != 2:
                print('Input should be 2 characters!')  # Error Message
                running = True  # Return to start of while loop
            else:
                running = True


# Gets enemy target coordinate
# By random rolling 0-7 twice
# Makes one column and the other row
# Adds two values to target list and returns target list
def get_enemy_target():
    target = []
    column = random.randrange(0, 8)
    row = random.randrange(0, 8)
    column = column_letter[column]
    target.append(column)
    target.append(row)
    return target


# Function responsible for checking if target(list) has already been tried
def check_if_tried(target, some_board):
    board_index = column_number[target[0].upper()]  # Board index(aka column) = 1st element's value:key in column_number
    board_row = target[1] - 1  # Board row(aka list) = 2nd element in target list
    if some_board[board_row][board_index] == "X" or board[board_row][board_index] == '$':
        return True  # Return true because X means its already been tried
    else:  # else
        return False  # False because it has not been tried


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
        print(ships)
        return True
    else:
        return False


def check_if_tried_enemy(target):
    board_index = target[0]  # Board index(aka column) = 1st element's value:key in column_number
    board_row = target[1]    # Board row(aka list) = 2nd element in target list
    if (myboard[board_row][board_index] == "X" or myboard[board_row][board_index] == '$'or
            myboard[board_row][board_index] == '*'):
        return True  # Return true because X means its already been tried
    else:  # else
        return False  # False because it has not been tried


def check_if_already_occupied(target):
    board_index = target[0]  # Board index(aka column) = 1st element's value:key in column_number
    board_row = target[1]    # Board row(aka list) = 2nd element in target list
    if myboard[board_row - 1][board_index] == "@":
        return True  # Return true because X means its already been tried
    else:  # else
        return False  # False because it has not been tried


# Function responsible for replacing 'O's with 'X's upon missing
# Takes list as input
def miss(target, some_board):
    column = column_number[target[0].upper()]  # Column = 1st element's value:key in column_number Dictionary
    row = (target[1] - 1)  # Row = Second element of target lst - 1( -1 makes it work correctly, not sure why)
    missed_target = [column, row]  # Consider slimming this function down
    board_index = missed_target[0]  # As a lot of this is not needed
    board_list = missed_target[1]  # Written like this to help understand what represented what
    some_board[board_list][board_index] = "X"  # In relation to the board


# Function responsible for replacing 'O's with '$'s upon hitting
# Takes target list as input [column, row]
def hit(target, some_board):
    column = column_number[target[0].upper()]  # Column = 1st element's value:key in column_number Dictionary
    row = (target[1] - 1)  # Row = Second element of target lst - 1( -1 makes it work correctly, not sure why)
    missed_target = [column, row]  # Consider slimming this function down
    board_index = missed_target[0]  # As a lot of this is not needed
    board_list = missed_target[1]  # Written like this to help understand what represented what
    some_board[board_list][board_index] = "$"  # In relation to the boar


def enemy_hit(target, some_board):
    column = column_number[target[0].upper()]  # Column = 1st element's value:key in column_number Dictionary
    row = (target[1] - 1)  # Row = Second element of target lst - 1( -1 makes it work correctly, not sure why)
    enemy_target = [column, row]  # Consider slimming this function down
    board_index = enemy_target[0]  # As a lot of this is not needed
    board_list = enemy_target[1]  # Written like this to help understand what represented what
    if some_board[board_list][board_index] == "@":  # In relation to the boar
        some_board[board_list][board_index] = '$'
        print('Enemy Hit!')
        return True
    else:
        return False


def enemy_miss(target, some_board):
    column = target[0]  # Column = 1st element's value:key in column_number Dictionary
    row = target[1]  # Row = Second element of target lst - 1( -1 makes it work correctly, not sure why)
    missed_target = [column, row]  # Consider slimming this function down
    board_index = missed_target[0]  # As a lot of this is not needed
    board_list = missed_target[1]  # Written like this to help understand what represented what
    some_board[board_list][board_index] = "X"  # In relation to the board


# Function that changes the board to reflect the destruction of a ship
# Changes all hit($) calls with destroyed(*) call
def destroy_ship(ship, some_board):
    for section in ship:  # for coordinate(list) in list of coordinates
        column = column_number[section[0].upper()]  # Column = 1st element's value:key in column_number Dictionary
        row = (section[1] - 1)  # Row = Second element of target lst - 1( -1 makes it work correctly, not sure why)
        missed_target = [column, row]  # Consider slimming this function down
        board_index = missed_target[0]  # As a lot of this is not needed
        board_list = missed_target[1]  # Written like this to help understand what represented what
        some_board[board_list][board_index] = "*"  # In relation to the board


def destroy_my_ship(ship):
    for section in ship:  # for coordinate(list) in list of coordinates
        for coord in section:
            column = coord[0]  # Column = 1st element's value:key in column_number Dictionary
            row = (coord[1] - 1)  # Row = Second element of target lst - 1( -1 makes it work correctly, not sure why)
            missed_target = [column, row]  # Consider slimming this function down
            board_index = missed_target[0]  # As a lot of this is not needed
            board_list = missed_target[1]  # Written like this to help understand what represented what
            myboard[board_list][board_index] = "*"  # In relation to the board
    print_board()


def place_ship(ship, some_board):
    for target in ship:
        column = target[0]   # Column = 1st element's value:key in column_number Dictionary
        row = target[1] - 1   # Row = Second element of target lst - 1( -1 makes it work correctly, not sure why)
        missed_target = [column, row]  # Consider slimming this function down
        board_index = missed_target[0]  # As a lot of this is not needed
        board_list = missed_target[1]  # Written like this to help understand what represented what
        some_board[board_list][board_index] = "@"  # In relation to the board


# Function that takes user inputted coordinates and checks for hit or miss
def player_turn(target):
    ships_clone = ships.copy()
    if valid_column(target) is True and valid_row(target) is True:
            if check_if_tried(target, board) is False:
                if target in ships[0]:
                    ships[0].remove(target)
                    hit(target, board)
                    print('Hit!')
                    if not ships[0]:
                        ships_clone.remove(ships[0])
                        destroy_ship(ship_1_damage, board)
                        print('You destroyed a Klingon Bird of Prey!')
                        if not ships_clone:
                                print('---You have destroyed the mighty Klingon Empire!---')
                elif target in ships[1]:
                    ships[1].remove(target)
                    hit(target, board)
                    print('Hit!')
                    if not ships[1]:
                        ships_clone.remove(ships[1])
                        destroy_ship(ship_2_damage, board)
                        print('You destroyed a Romulan War Bird!')
                        if not ships_clone:
                            print('---You have pushed the Romulans back into the Neutral Zone!---')  # You dun won!
                elif target in ships[2]:
                    ships[2].remove(target)
                    hit(target, board)
                    print('Hit!')
                    if not ships[2]:
                        ships_clone.remove(ships[2])
                        destroy_ship(ship_3_damage, board)
                        print('You have destroyed a Borg Cube!')
                        if not ships_clone:
                                print('---You have prevented the assimilation of mankind!---')  # You dun won!
                else:  # Else
                    miss(target, board)  # Run miss function on target list
                    print('Miss!')
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

next_targets = []


def get_next_targets(some_target):
    if some_target[0] == 1:
        up = copy.deepcopy(some_target)
        down = copy.deepcopy(some_target)
        right = copy.deepcopy(some_target)
        up[1] -= 1
        down[1] += 1
        right[0] += 1
        next_targets.append(up)
        next_targets.append(down)
        next_targets.append(right)
        if some_target[1] == 0:
            next_targets.remove(up)
        elif some_target[1] == 7:
            next_targets.remove(down)
    elif some_target[0] == 8:
        up = copy.deepcopy(some_target)
        down = copy.deepcopy(some_target)
        left = copy.deepcopy(some_target)
        up[1] -= 1
        down[1] += 1
        left[0] -= 1
        next_targets.append(up)
        next_targets.append(down)
        next_targets.append(left)
        if some_target[1] == 0:
            next_targets.remove(up)
        elif some_target[1] == 7:
            next_targets.remove(down)
    elif some_target[1] == 0:
        down = copy.deepcopy(some_target)
        left = copy.deepcopy(some_target)
        right = copy.deepcopy(some_target)
        down[1] += 1
        left[0] -= 1
        right[0] += 1
        next_targets.append(down)
        next_targets.append(left)
        next_targets.append(right)
    elif some_target[1] == 7:
        up = copy.deepcopy(some_target)
        left = copy.deepcopy(some_target)
        right = copy.deepcopy(some_target)
        up[1] -= 1
        left[0] -= 1
        right[0] += 1
        next_targets.append(up)
        next_targets.append(left)
        next_targets.append(right)
    else:
        up = copy.deepcopy(some_target)
        down = copy.deepcopy(some_target)
        left = copy.deepcopy(some_target)
        right = copy.deepcopy(some_target)
        up[1] -= 1
        down[1] += 1
        left[0] -= 1
        right[0] += 1
        next_targets.append(up)
        next_targets.append(down)
        next_targets.append(left)
        next_targets.append(right)


def enemy_turn(myships_clone, a, b, c):
    if len(next_targets) >= 1:
        getting_target = True
        while getting_target:
            enemy_target = next_targets.pop()
            if check_if_tried_enemy(enemy_target) is False:
                getting_target = False
                column = enemy_target[0]
                row = enemy_target[1]  # Row = Second element of target lst - 1( -1 makes it work correctly
                target = [column, row]  # Consider slimming this function down
                last_target = [column, row]
                board_index = target[0]  # As a lot of this is not needed
                board_list = target[1]  # Written like this to help understand what represented what
                target[0] = column_letter[target[0]]
                target[1] += 1
                print(target)
                target[0] = column_number[target[0]]
                if myboard[board_list][board_index] == "@":  # In relation to the boar
                    myboard[board_list][board_index] = "$"
                    print('Enemy Hit!')
                    get_next_targets(last_target)
                    if target in myships_clone[0][0]:
                        myships_clone[0][0].remove(target)
                        if not myships_clone[0][0]:
                            destroy_my_ship(a)
                            print('Enemy has destroyed the Defiant!')
                            myships.remove(myships_clone[0])
                            next_targets.clear()
                            if not myships:
                                print_board()
                                print('---The Dominion has taken DeepSpace 9  and invaded the Alpha Quadrant---')
                    elif target in myships_clone[1][0]:
                        myships_clone[1][0].remove(target)
                        if not myships_clone[1][0]:
                            destroy_my_ship(b)
                            print('Enemy has destroyed Voyager!')
                            myships.remove(myships_clone[1])
                            next_targets.clear()
                            if not myships:
                                print_board()
                                print('---The Borg have taken control of the bridge!---')
                                print('---ACTIVATE SELF DESTRUCT SEQUENCE JAYNEWAY-ALPHA-3359---')
                    elif target in myships_clone[2][0]:
                        myships_clone[2][0].remove(target)
                        if not myships_clone[2][0]:
                            destroy_my_ship(c)
                            print('Enemy has destroyed The Enterprise!')
                            myships.remove(myships_clone[2])
                            next_targets.clear()
                            if not myships:
                                print_board()
                                print('---The Borg have assimilated Capt. Jean Luc Picard!---')
                else:  # Else
                    enemy_miss(enemy_target, myboard)  # Run miss function on target list
                    print('Enemy Miss!')
            else:
                getting_target = True
    else:
        getting_unused_target = True
        while getting_unused_target:
            enemy_target = []
            column = random.randrange(1, 9)
            row = random.randrange(0, 8)
            enemy_target.append(column)
            enemy_target.append(row)
            if check_if_tried_enemy(enemy_target) is False:
                getting_unused_target = False
                column = enemy_target[0]
                row = enemy_target[1]  # Row = Second element of target lst - 1( -1 makes it work correctly
                target = [column, row]  # Consider slimming this function down
                last_target = [column, row]
                board_index = target[0]  # As a lot of this is not needed
                board_list = target[1]  # Written like this to help understand what represented what
                target[0] = column_letter[target[0]]
                target[1] += 1
                print(target)
                target[0] = column_number[target[0]]
                if myboard[board_list][board_index] == "@":  # In relation to the boar
                    myboard[board_list][board_index] = "$"
                    print('Enemy Hit!')
                    get_next_targets(last_target)
                    if target in myships_clone[0][0]:
                        myships_clone[0][0].remove(target)
                        if not myships_clone[0][0]:
                            destroy_my_ship(a)
                            print('Enemy has destroyed the Defiant!')
                            myships.remove(myships_clone[0])
                            next_targets.clear()
                            if not myships:
                                print_board()
                                print('---The Dominion has taken DeepSpace 9  and invaded the Alpha Quadrant---')
                    elif target in myships_clone[1][0]:
                        myships_clone[1][0].remove(target)
                        if not myships_clone[1][0]:
                            destroy_my_ship(b)
                            print('Enemy has destroyed Voyager!')
                            myships.remove(myships_clone[1])
                            next_targets.clear()
                            if not myships:
                                print_board()
                                print('---The Borg have taken control of the bridge!---')
                                print('---ACTIVATE SELF DESTRUCT SEQUENCE JAYNEWAY-ALPHA-3359---')
                    elif target in myships_clone[2][0]:
                        myships_clone[2][0].remove(target)
                        if not myships_clone[2][0]:
                            destroy_my_ship(c)
                            print('Enemy has destroyed The Enterprise!')
                            myships.remove(myships_clone[2])
                            next_targets.clear()
                            if not myships:
                                print_board()
                                print('---The Borg have assimilated Capt. Jean Luc Picard!---')
                else:  # Else
                    enemy_miss(enemy_target, myboard)  # Run miss function on target list
                    print('Enemy Miss!')
            else:
                getting_unused_target = True


# Function that gathers input on rather user wishes to continue playing
def play_again():
    print('Would You like to play again?')
    go_again = input('Type \'EXIT\' to quit, or press ENTER to play again:  ')
    return go_again


def main():
    running = True
    while running:
        filling = True
        clear_lists()  # Clear all non referenced global lists
        fill_boards()
        hide_ships(bird_of_prey, war_bird, borg_cube)
        #ships_hidden = 0
        # The below if statements makes sure no ship coordinates overlap, and if so, will restart loop.
        # Consider finding a way to make it only re-randomize overlapped ship coordinates
        if any(True for i in war_bird if i in bird_of_prey):
            filling = False
        if any(True for z in borg_cube if z in war_bird):
            filling = False
        if any(True for k in bird_of_prey if k in borg_cube):
            filling = False
        while filling is False:  # If a ship coordinate is pegged asa repeated
            main()  # Program restarts and tries again
        print_board()
        hide_myships(defiant)
        hide_myships(voyager)
        hide_myships(enterprise)
        ship_1_damage.extend(bird_of_prey)  # Creates copies
        ship_2_damage.extend(war_bird)  # of all three ships
        ship_3_damage.extend(borg_cube)  # to be referenced by the destroy_ship function
        ships.append(bird_of_prey)  # Adds all three ships
        ships.append(war_bird)  # To a single list(ships)
        ships.append(borg_cube)  # To be used to keep track of current ships in play
        myship_1_damage = copy.deepcopy(defiant)  # to be referenced by the destroy_ship function
        myship_2_damage = copy.deepcopy(voyager)
        myship_3_damage = copy.deepcopy(enterprise)
        myships.append(defiant)
        myships.append(voyager)
        myships.append(enterprise)
        playing = True
        timer = 5
        print('Game Will be begin in....')
        myships_clone = myships.copy()
        while timer > 0:
            print(timer)
            timer -= 1
            time.sleep(1)
        while playing:
            print_board()
            player_target = get_target()
            print('CHARGING STARBOARD PHASER BANKS')
            #time.sleep(2)
            player_turn(player_target)
            print_board()
            time.sleep(2)
            print('Enemy is charging his lazors!')
            time.sleep(2)
            print('ENEMY IS FIRING HIS LAZORS!!!!!!')
            #time.sleep(1)
            enemy_turn(myships_clone, myship_1_damage, myship_2_damage, myship_3_damage)
            if len(ships[0]) == 0 and len(ships[1]) == 0 and len(ships[2]) == 0:
                break
            if len(myships_clone[0][0]) == 0 and len(myships_clone[1][0]) == 0 and len(myships_clone[2][0]) == 0:
                break
        if play_again() == "":  # Runs play again function and if user hits enter
            print('The Game will restart in 5 seconds')
            timer = 5  # Timer
            while timer > 0:  # While timer  > 0(Not done)
                time.sleep(1)  # Wait 1 sec
                print(timer)  # print timer var
                timer -= 1  # timer var - 1 and equal to the result
            running = True
        else:
            break
