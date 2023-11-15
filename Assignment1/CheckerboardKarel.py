"""
File: CheckerboardKarel.py
Name: 
----------------------------
pre-condition: Karel is at Street 1, Avenue 1, facing East
post-condition: Karel is free to stand at any point and face any direction.
Goal: The world should look like a chess board with beepers no matter what size the world is!
"""

from karel.stanfordkarel import *


def main():
    """
    Karel fills in intervals layer go and forth the right and left side by layer from the bottom.
    """
    put_beeper()
    while facing_east():
        go()
    pass


def go():
    go_rightwards()
    go_leftwards()


def go_rightwards():
    """
    per-condition: Karel is on beeper
    post-condition: Karel is at the far left on the line of "the row to the left"
    There are 3 condition:
    1.When there are more than 2 spaces in front of Karel => Karel moves 2 points, puts beeper
    2.When there is 1 space + the wall in front of Karel => Karel moves 1 point, turns left and moves 1 point, turns left, puts beeper
    3.front is a wall => Karel turns left, moves 1 point, turns left and moves 2 points, puts beeper
    The first method cannot be part of a loop.
    """
    while facing_east():
        if not front_is_clear():
            turn_left()
            move()
            turn_left()
            move()
            put_beeper()
        else:
            move()
            if not front_is_clear():
                turn_left()
                move()
                turn_left()
                put_beeper()
            else:
                move()
                put_beeper()


def go_leftwards():
    """
    per-condition: Karel is on beeper
    post-condition: Karel is at the far left on the line of "the row to the left"
    There are 3 condition:
    1.When there are more than 2 spaces in front of Karel => Karel moves 2 points, puts beeper
    2.When there is 1 space + the wall in front of Karel => Karel moves 1 point, turns left and moves 1 point, turns left, puts beeper
    3.front is a wall => Karel turns left, moves 1 point, turns left and moves 2 points, puts beeper
    The first method cannot be part of a loop.
    """
    while facing_west():
        if not front_is_clear():
            turn_right()
            move()
            turn_right()
            move()
            move()
            put_beeper()
        else:
            move()
            if not front_is_clear():
                turn_right()
                move()
                turn_right()
                put_beeper()
            else:
                move()
                put_beeper()


def turn_around():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
