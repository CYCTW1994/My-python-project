"""
File: StoneMasonKarel.py
Name: Cara
--------------------------------
Pre-condition: Karel is at Street1, Avenue 1, where is the first pillar,
facing East. The wall is behind Karel.
Post-condition: Karel is on the far right of the Street 1, where is the last pillar,
facing East. The wall is in front of Karel.
Action: Instruct Karel to build a column (a vertical structure that is 5 beepers tall)
in each avenue that is either on the right or left side of the arch.
Goal: To make the pillar complete, and the number of beepers in each position is only one.
Other Remarks:
1) The distance between each pillar is always 3 pillars no matter in which worlds.
2) Karel needs to be able to do the works in different worlds with the same distance between arches.
"""

from karel.stanfordkarel import *


def main():
    """
    3 steps for Karel to do the job:
    1) go checking and repairing (= put beeper)
    2) climb down the pillar after finishing the repair
    3) walk to the next damaged pillar
    """
    while front_is_clear():
        check_and_repair_pillar()
        climb_down()
        walk_to_next_pillar()
    check_and_repair_pillar()
    climb_down()
    walk_to_next_pillar()


def check_and_repair_pillar():
    """
    Karel turns left first to start climbing up to check.
    """
    turn_left()
    while front_is_clear():
        check_situation1()
    check_situation2()


def check_situation1():
    if on_beeper():
        move()
    else:
        put_beeper()
        move()


def check_situation2():
    if on_beeper():
        turn_around()
    else:
        put_beeper()
        turn_around()


def turn_around():
    for i in range(2):
        turn_left()


def climb_down():
    while front_is_clear():
        move()
    turn_left()


def walk_to_next_pillar():
    if front_is_clear():
        for i in range(4):
            move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
