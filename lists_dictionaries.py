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

next_targets = []