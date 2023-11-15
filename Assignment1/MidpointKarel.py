"""
File: MidpointKarel.py
Name: Cara
----------------------------
Pre-condition: Karel is at Street 1, Avenue 1, facing East.
Post-condition: Karel is in the middle point(or either of the
two central corners if 1st Street has an even number of corners)
of Street 1 and leave only 1 beeper at where Karel stays in the world.
"""

from karel.stanfordkarel import *


def main():
    """
    1. Karel puts 1 beeper on the Street 1, Avenue 1, and move.
    2. Karel starts to put a beeper back and forth in the east and west direction.
    3. When Karel is at the middle points, she puts 2 beepers.
    4. Karel begins to pick up a beeper at each point along Street 1.
    5. There will be 1 beeper left at the middle point, Karel goes there.
    """
    put_beeper()
    first_check()
    beeper_all_the_way()
    clean_way()
    back_to_middle()


def first_check():
    if not front_is_clear():
        pass
    else:
        move()


def beeper_all_the_way():
    """
    Pre-condition: Karel is at Street 1, Avenue 2, facing East.
    Post-condition: Karel is at the middle point of Street 1 with 1 beeper.
    """
    while not on_beeper():
        west_to_east()
        east_to_west()


def west_to_east():
    """
    Pre-condition: Karel is not on beeper, facing east
    Post-condition: Karel is not on beeper, facing west
    Action: Karel puts 1 beeper and then walk to the vacancy on the opposite side, and then turn around.
    If there is no any vacancy in front of Karel then Karel
    has to put 2 beepers at the last location where she stays.
    """
    while front_is_clear():
        move()
    turn_around()
    west_to_east_return()


def west_to_east_return():
    # Karel is in front of the wall, facing West and getting ready to put beeper on the vacancy.
    if not on_beeper():
        put_beeper()
        move()
    else:
        move()
        while on_beeper():
            move()
        middle_point_judgement()


def middle_point_judgement():
    # To judge if Karel is at the middle point.
    move()
    if on_beeper():
        turn_around()
        move()
        put_2_beeper()
    else:
        turn_around()
        move()
        put_beeper()
        turn_around()
        move()


def east_to_west():
    # Karel is facing West and getting ready to go East.
    while front_is_clear():
        move()
    turn_around()
    west_to_east_return()


def east_to_west_return():
    # Karel is in front of the wall, facing East and getting ready to go putting beeper on the vacancy.
    if on_beeper():
        move()
        while on_beeper():
            move()
        middle_point_judgement()


def clean_way():
    """
    Karel from the middle point to the wall, and start to pick up 1 beeper at each point on Street 1.
    Pre-condition: Karel is at the middle point.
    Post-condition: Karel is in front of the wall.
    """
    back_to_wall()
    pick_beeper_each_point()


def back_to_wall():
    if facing_east():
        turn_around()
    else:
        while front_is_clear():
            move()
        move()


def pick_beeper_each_point():
    pick_beeper()
    while front_is_clear():
        move()
        pick_beeper()
    turn_around()


def back_to_middle():
    # Karel is in front of the wall, ready to go to the middle point where there is 1 beeper.
    while not on_beeper():
        move()


def put_2_beeper():
    put_beeper()
    put_beeper()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
