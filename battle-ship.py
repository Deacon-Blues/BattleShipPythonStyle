__author__ = 'Terrance'

import random

# First item is column second item is row
ship = []

board = []  # Empty list to be populated by fill_board function

x = ['1', '2', '3', '4', '5']

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


def random_row():
    random.randrange(1, 6)


def random_column():
    random.randrange(1, 6)


def hide_ship():
    ship.append(random_column())  # sets first item in ship to column
    ship.append(random_row())  # sets second item in ship to row


def shoot():
    turn = 0
    while turn < 10:
        column = input('What column?: ')
        row = input('What row?: ')
        column = int(column)
        row = int(row)
        target = [column, row]
        if target == ship:
            turn = 10
            print('Hit! You win!')
        else:
            turn += 1
            print('Miss! Try again!')


def main():
    fill_board()
    print_board()
    hide_ship()
    shoot()
main()