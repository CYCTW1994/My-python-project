"""
File: hailstone.py
Name: Cara
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


ONLY = 1


def main():
    """
    greetings-> user to enter a number -> end if enter 1 -> if not 1
    then automatically run the while loop formula -> summary(count steps)
    """
    print('This program computes Hailstone sequences.')
    n = int(input('Enter a number: '))
    go(n)


def go(a):
    s = 0
    while a != 1:
        s += 1
        if a % 2 == 0:
            e = a / 2
            print(str(a) + ' is even, so I take half: ' + str(e))  # 前面的a怎麼表示????????????
            a = e
        else:
            o = 3 * a + 1
            print(str(a) + ' is odd, so I make 3n+1: ' + str(o))
            a = o
    print('It took ' + str(s) + ' steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
