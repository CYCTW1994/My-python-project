"""
File: class_reviews.py
Name: Cara
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""
CLASS1 = 'SC001'
CLASS2 = 'SC101'
EXIT = '-1'

def main():
    """
    Users key-in the class and score, and print out the summary by each class
    4 situations:
    1) There are scores in SC001 & SC101.
    2) There is no score in SC001 but SC101.
    3) There is no score in SC101 but SC001.
    4) no score in both SC001 & SC101.
    """
    max001 = -float("inf")    # inf means infinite, it is the only workable word in float.
    max101 = -float("inf")
    min001 = float("inf")
    min101 = float("inf")
    ttl001 = 0
    ttl101 = 0
    count001 = 0
    count101 = 0
    while True:
        class_name = input('Which class? ')
        new_class_name = class_name.upper()
        if new_class_name == EXIT:
            break
        if new_class_name == CLASS1:
            score = int(input('Score: '))
            if score > max001:
                max001 = score
            if score < min001:
                min001 = score
            ttl001 += score
            count001 += 1
            avg001 = ttl001 / count001
        else:
            score = int(input('Score: '))
            if score > max101:
                max101 = score
            if score < min101:
                min101 = score
            ttl101 += score
            count101 += 1
            avg101 = ttl101 / count101
    if count001 == 0 and count101 ==0:
        print('No class scores were entered')
    else:
        print('=============SC001=============')
        if count001 == 0:
            print('No score for SC001')
        else:
            print('Max (001): ' + str(max001))
            print('Min (001): ' + str(min001))
            print('Avg (001): ' + str(avg001))
        print('=============SC101=============')
        if count101 == 0:
            print('No score for SC101')
        else:
            print('Max (101): ' + str(max101))
            print('Min (101): ' + str(min101))
            print('Avg (101): ' + str(avg101))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
