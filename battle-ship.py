__author__ = 'Terrance'

import random
import time
import copy

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

board = []  # Empty list to be populated by fill_board function

myboard = []

x = []  # List of row numbers, inserted into the front of each row later on

columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

rows = [1, 2, 3, 4, 5, 6, 7, 8]

y = [" ", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # Needs space to properly print in 8x8 grid

# First item is column second item is row
# Lists that contain ship coordinates
ship_1 = []
ship_2 = []
ship_3 = []

myship_1 = []
myship_2 = []
myship_3 = []
# Lists that are used to hold ship coordinates and later, change the board
ship_1_damage = []
ship_2_damage = []
ship_3_damage = []
# Holds all current possible hit targets
ships = []
myships = []


# Clears  a given list and returns it
def clear_lst(lst):
    lst.clear()
    return lst


# Function that clears a number of lists and returns them
def clear_lists():
    clear_lst(ships)
    clear_lst(ship_1)
    clear_lst(ship_2)
    clear_lst(ship_3)
    clear_lst(ship_1_damage)
    clear_lst(ship_2_damage)
    clear_lst(ship_3_damage)
    clear_lst(myships)
    clear_lst(myship_1)
    clear_lst(myship_2)
    clear_lst(myship_3)


# Function responsible for creating 8 lists of 8 O's
def fill_board(some_board):
    for i in range(0, 8):
        some_board.append(['O'] * 8)  # Adds 8 lists of 8 'O's to board list


# Refills x list with numbers 1-8 in string form
def fill_x(lst):
    for number in range(1, 9):
        lst.append(str(number))


# Function responsible for inserting 1-8 at the front of each list
def fill_grid(some_board):
    fill_x(x)
    for row, i in zip(some_board, x):  # Used Zip function to loop through 2 separate lists
        row.insert(0, str(i))  # Insert the first number from the x list at the front


def fill_boards():
    clear_lst(myboard)  # Clear global myboard list
    clear_lst(board)  # Clear global board list
    fill_board(board)  # populates board list with appropriate number of O's
    fill_grid(board)  # adds the row labels to board list
    fill_board(myboard)  # populates myboard list with appropriate number of O's
    fill_grid(myboard)  # adds row labels to myboard list


# Function responsible for printing board list as a 8x8 grid
def print_board():
    print("  ".join(y), '\t', "  ".join(y))
    for row, row_again in zip(board, myboard):
        print("  ".join(row), '\t', "  ".join(row_again))


def random_column_key():
    return random.randrange(2, 8)


# Converts column values to their int counterparts
def convert_column(ship_origin, port, starboard):
    ship_origin[0] = column_letter[ship_origin[0]]
    port[0] = column_letter[port[0]]
    starboard[0] = column_letter[starboard[0]]


# Function that takes random number functions as coordinates
def hide_ship(ship):
    port = []  # Empty list, will represent ship origin coordinates + 1
    starboard = []  # Empty list, will represent ship origin coordinates - 1
    ship_origin = []
    direction = random.randrange(1, 3)
    if direction == 1:
        ship_origin.append(random_column_key())  # sets first item in ship to column
        ship_origin.append(random.randrange(2, 8))  # sets second item in ship to row
        port.append(ship_origin[0])  # Adds origin column to port list
        port.append(ship_origin[1] + 1)  # Adds origin row + 1 to port list
        starboard.append(ship_origin[0])  # Adds origin column to starboard list
        starboard.append(ship_origin[1] - 1)  # Adds origin row - 1 to starboard list
        convert_column(ship_origin, port, starboard)
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
        convert_column(ship_origin, port, starboard)
        ship.append(ship_origin)  # Adds origin coordinates to ship list
        ship.append(port)  # Adds port coordinates to ship list
        ship.append(starboard)  # Adds starboard coordinates to ship list


def hide_ships(one, two, three):
        hide_ship(one)  # Randomizes and checks coordinates for ship_1 list
        hide_ship(two)  # Randomizes and checks coordinates for ship_2 list
        hide_ship(three)  # Randomizes and checks coordinates for ship_3 list


def get_ship_origin(staging_ground):
    running = True
    while running:
        print('Remember: The Ship will extend to the spaces directly above and below the ship origin.')
        print('Watch out for the end of the board!!!')
        ship_origin = input('Enter Ship origin: ')
        column = column_number[ship_origin[0].upper()]
        row = ship_origin[1]
        row = int(row)
        coord = [column, row]
        if check_if_already_occupied(coord) is False:
            board_index = column  # As a lot of this is not needed
            board_list = row - 1  # Written like this to help understand what represented what
            myboard[board_list][board_index] = '@'
            staging_ground.append(coord)
            running = False
        else:
            running = True


def extend_ship_vertical(staging_ground):
    port = []
    starboard = []
    staging_ground_clone = copy.deepcopy(staging_ground)
    staging_ground_clone[0][1] += 1
    port.append(staging_ground_clone[0][0])
    port.append(staging_ground_clone[0][1])
    staging_ground_clone[0][1] -= 2
    starboard.append(staging_ground_clone[0][0])
    starboard.append(staging_ground_clone[0][1])
    staging_ground.append(port)
    staging_ground.append(starboard)


def extend_ship_horizontal(staging_ground):
    port = []
    starboard = []
    staging_ground_clone = copy.deepcopy(staging_ground)
    staging_ground_clone[0][0] += 1
    port.append(staging_ground_clone[0][0])
    port.append(staging_ground_clone[0][1])
    staging_ground_clone[0][0] -= 2
    starboard.append(staging_ground_clone[0][0])
    starboard.append(staging_ground_clone[0][1])
    staging_ground.append(port)
    staging_ground.append(starboard)


def hide_myships(ship):
    main_staging_ground = []
    get_ship_origin(main_staging_ground)
    print('Would you like to place your ship [V]ertical or [H]orizontal: ')
    v_or_h = input('Enter: V for Vertical or H for horizontal: ')
    if v_or_h == 'V':
        extend_ship_vertical(main_staging_ground)
    elif v_or_h == 'H':
        extend_ship_horizontal(main_staging_ground)
    else:
        print('Error101')
    ship.append(main_staging_ground)
    print('----------------------SHIP DEPLOYED-----------------------')
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
    if myboard[board_row][board_index] == "@":
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
                        print('YOU SANK THE NORTH KOREAN FLAG SHIP!')
                        if not ships_clone:
                                print('---YOU HAVE SANK THE KOREAN FLEET! YOU ARE NOW GLORIOUS LEADER---')
                elif target in ships[1]:
                    ships[1].remove(target)
                    hit(target, board)
                    print('Hit!')
                    if not ships[1]:
                        ships_clone.remove(ships[1])
                        destroy_ship(ship_2_damage, board)
                        print('YOU SANK AN ENEMY SHIP! MUCH WOW REALLY BOOM!')
                        if not ships_clone:
                            print('---YOU WIN: PLAYER RECEIVES 4.20 DODGE COINS---')  # You dun won!
                elif target in ships[2]:
                    ships[2].remove(target)
                    hit(target, board)
                    print('Hit!')
                    if not ships[2]:
                        ships_clone.remove(ships[2])
                        destroy_ship(ship_3_damage, board)
                        print('SHIELDS FAILING! THEIR WARP COILS ARE VENTING PLASMA: BREACH IMMINENT!')
                        if not ships_clone:
                                print('---BOOM HEADSHOT, YOU SANK HIS BRAP SHIP!---')  # You dun won!
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


def enemy_turn(myships_clone, a, b, c):
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
            board_index = target[0]  # As a lot of this is not needed
            board_list = target[1]  # Written like this to help understand what represented what
            target[0] = column_letter[target[0]]
            target[1] += 1
            print(target)
            target[0] = column_number[target[0]]
            if myboard[board_list][board_index] == "@":  # In relation to the boar
                myboard[board_list][board_index] = "$"
                print('Enemy Hit!')
                if target in myships_clone[0][0]:
                    myships_clone[0][0].remove(target)
                    if not myships_clone[0][0]:
                        destroy_my_ship(a)
                        print('YOUR GLORIOUS FLAG SHIP IS NO MORE! CUT RICE STIPENDS QUUIIICKKK!!!!')
                        myships_clone.remove(myships_clone[0])
                        if not myships_clone:
                            print('---YOU LOST THE KOREAN FLEET! YOU ARE NOW SHITTY RICE MONGER---')
                elif target in myships_clone[1][0]:
                    myships_clone[1][0].remove(target)
                    if not myships_clone[1][0]:
                        destroy_my_ship(b)
                        print('YOUR SHIPS IS TEH DEAD! MUCH SAD, REALLY WOW!')
                        myships_clone.remove(myships_clone[1])
                        if not myships_clone:
                            print('---YOU LOOSE: PLAYER ACCOUNT DEDUCTED 4.20 DODGE COINS---')
                elif target in myships_clone[2][0]:
                    myships_clone[2][0].remove(target)
                    if not myships_clone[2][0]:
                        destroy_my_ship(c)
                        print('WE\'RE VENTING PLASMA FROM THE PORT NACELLE! ALL HANDS TO ESCAPE PODS!!! ')
                        myships_clone.remove(myships_clone[2])
                        if not myships_clone:
                            print('---ACTIVATE SELF DESTRUCT SEQUENCE JAYNEWAY-ALPHA-3359---')
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
        hide_ships(ship_1, ship_2, ship_3)
        #ships_hidden = 0
        # The below if statements makes sure no ship coordinates overlap, and if so, will restart loop.
        # Consider finding a way to make it only re-randomize overlapped ship coordinates
        if any(True for i in ship_2 if i in ship_1):
            filling = False
        if any(True for z in ship_3 if z in ship_2):
            filling = False
        if any(True for k in ship_1 if k in ship_3):
            filling = False
        while filling is False:  # If a ship coordinate is pegged asa repeated
            main()  # Program restarts and tries again
        print_board()
        hide_myships(myship_1)
        hide_myships(myship_2)
        hide_myships(myship_3)
        ship_1_damage.extend(ship_1)  # Creates copies
        ship_2_damage.extend(ship_2)  # of all three ships
        ship_3_damage.extend(ship_3)  # to be referenced by the destroy_ship function
        ships.append(ship_1)  # Adds all three ships
        ships.append(ship_2)  # To a single list(ships)
        ships.append(ship_3)  # To be used to keep track of current ships in play
        myship_1_damage = list(myship_1)  # to be referenced by the destroy_ship function
        myship_2_damage = list(myship_2)
        myship_3_damage = list(myship_3)
        myships.append(myship_1)
        myships.append(myship_2)
        myships.append(myship_3)
        playing = True
        timer = 5
        print('Game Will be begin in....')
        myships_clone = copy.deepcopy(myships)
        while timer > 0:
            print(timer)
            timer -= 1
            time.sleep(1)
        while playing:
            print_board()
            player_target = get_target()
            print('CHARGING STARBOARD PHASER BANKS')
            time.sleep(2)
            player_turn(player_target)
            print_board()
            time.sleep(2)
            print('Enemy is charging his lazors!')
            time.sleep(2)
            print('ENEMY IS FIRING HIS LAZORS!!!!!!')
            time.sleep(1)
            enemy_turn(myships_clone, myship_1_damage, myship_2_damage, myship_3_damage)
            if len(ships[0]) == 0 and len(ships[1]) == 0 and len(ships[2]) == 0:
                break
            if len(myships_clone) == 0:
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
main()