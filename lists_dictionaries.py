__author__ = 'Deacon-Blues'

# Dictionary, column number as value, column letter as key
column_letter = {1: 'A',
                 2: 'B',
                 3: 'C',
                 4: 'D',
                 5: 'E'}
# Dictionary, column letter as value, column letter as key
column_number = {'A': 1,
                 'B': 2,
                 'C': 3,
                 'D': 4,
                 'E': 5}

# First item is column second item is row
ship = []

board = []  # Empty list to be populated by fill_board function

x = ['1', '2', '3', '4', '5']  # List of row numbers, inserted into the front of each row later on

y = [" ", 'A', 'B', 'C', 'D', 'E']  # Needs space to properly print in 5x5 grid