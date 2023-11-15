"""
File: CollectNewspaperKarel.py
Name: Cara
--------------------------------
pre-condition: Karel is in the northwest corner (Street 4, Avenue 3) of the house, facing east.
post-condition: Karel is in the northwest corner (Street 4, Avenue 3) of the house, facing east.
Action: Instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course) at Street 3, Avenue 6, and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    2 steps to do:
    1) walk_out: Karel walks out to pick up the newspaper
    2) pickup_gohome_putdown: Karel brings the newspaper inside the house
    to the initial place and then put the newspaper down.
    """
    walk_out()
    pickup_gohome_putdown()


def walk_out():
    """
    Karel walks out of the house along the wall
    to where the beeper is outside the house.
    """
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_left()
    move()


def pickup_gohome_putdown():
    """
    Karel picks up the newspaper and returns to the pre-condition
    along the original path and puts down the newspaper.
    """
    pick_beeper()
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
