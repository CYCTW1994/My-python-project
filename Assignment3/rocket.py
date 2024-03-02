"""
File: rocket.py
Name: Cara
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 2


def main():
    """
    decomposition the body into 4 different parts and define them with "for i in range" and "for loop"
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(' ', end='')
        for j in range(i+1):
            print('/', end='')
        for j in range(i+1):
            print('\\', end='')
        for j in range(SIZE - i):
            print(' ', end='')
        print('')


def belt():
    for i in range(1):
        for j in range(1):
            print('+', end='')
        for j in range(SIZE*2):
            print('=', end='')
        for j in range(1):
            print('+', end='')
        print('')


def upper():
    for i in range(SIZE):
        for j in range(1):
            print('|', end='')
        for j in range(SIZE-1-i):
            print('.', end='')
        for j in range(i+1):
            print('/\\', end='')
        for j in range(SIZE-1-i):
            print('.', end='')
        for j in range(1):
            print('|', end='')
        print('')


def lower():
    for i in range(SIZE):
        for j in range(1):
            print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range(SIZE - i):
            print('\\/', end='')
        for j in range(i):
            print('.', end='')
        for j in range(1):
            print('|', end='')
        print('')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
