__author__ = 'Deacon-Blues'


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

columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # List of all Column letter values

rows = [1, 2, 3, 4, 5, 6, 7, 8]  # List of Row values, also used to verify input

y = [" ", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # List used to print column values in board. Space is for formatting

# |==================================================================|
# |=================ATTENTION====VERY IMPORTANT======================|
# |=====FIRST ITEM IN LIST IS COLUMN SECOND ITEM IN LIST IS ROW======|
# |=========TRUE FOR EVERY LIST CONTAINING SHIP COORDINATES==========|
# |==================================================================|
# |==================================================================|

# Lists that contain ship coordinates

# Lists used to store enemy ship coordinates
bird_of_prey = []
war_bird = []
borg_cube = []

# Lists used to store player ship coordinates
defiant = []
voyager = []
enterprise = []

# Lists that mirror enemy ship coordinates lists. Used to 'destroy' enemy ships
# The coordinates in the lists are fed to the destroy_ship function
# The destroy_ship function then changes the corresponding coordinates to '*'
ship_1_damage = []
ship_2_damage = []
ship_3_damage = []

# Lists that hold all ship coordinates

# Enemy ship Coordinates
ships = []

# Player Ship coordinates
myships = []