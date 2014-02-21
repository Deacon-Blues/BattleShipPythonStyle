__author__ = 'Deacon-Blues'

# Dictionary, column letter as value, column number as key
column_letter = {1: 'A',
                 2: 'B',
                 3: 'C',
                 4: 'D',
                 5: 'E'}

column_number = {'A': 1,
                 'B': 2,
                 'C': 3,
                 'D': 4,
                 'E': 5}

x = ['1', '2', '3', '4', '5']  # List of row numbers, inserted into the front of each row later on

columns = ['A', 'B', 'C', 'D', 'E']

rows = [1, 2, 3, 4, 5]

# First item is column second item is row
ship_origin = []

ship = []

board = []  # Empty list to be populated by fill_board function

y = [" ", 'A', 'B', 'C', 'D', 'E']  # Needs space to properly print in 5x5 grid