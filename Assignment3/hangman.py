"""
File: hangman.py
Name: Cara
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7   # chances to guess


def main():
    """
    make a flexible dash line => set for i in range(i=7) => enter letter
    => to see the location(i) of letter
    => if correct then replace the dash
    """
    word = random_word()
    length = len(word)
    dash = ''
    for i in range(len(word)):
        dash += '-'
    print('The word looks like: ' + dash)
    print('You have 7 wrong guesses left.')
    n = N_TURNS
    letter = int(input('Your guess: '))
    if letter.isalpha():
        if len(letter) == 1:
            letter = letter.upper()
            n -= 1
        else:
            print('Illegal format.')
    else:
        print('Illegal format.')
    guess(word, letter)
    if str(guess) == 'You are correct!':
        n += 1
        print('You are correct!')
    else:
        print('There is no ' + str(letter) + "'s in the world.")
    looks_like = replace(dash, letter, word)
    if str(looks_like) != word:
        if n == 0:
            print('You are completely hung :(')
        else:
            print('The word looks like: ' + str(looks_like))
            print('You have ' + n + ' wrong guesses left.')
    else:
        print('You win!!')


def guess(word, letter):
    ans = ''
    if word.find(letter):
        return 'You are correct!'
    else:
        return 'NO'


def replace(dash, letter, word):
    ans = ''
    s = word
    for i in range(len(s)):
        ''





    for i in range(N_TURNS):
        letter = int(input('Your guess: '))
        outcome = guess(dash, letter, word)   # if the letter is included in the word
        print(str(outcome))
        # "u r correct" or "there is no..."
        a = i
        if outcome != 'You are correct!':
            a == a+1
        looks_like = replace(dash, letter, word)
        if looks_like != word:
            print('The word looks like: ' + str(looks_like))
        else:
            print('You win!!')
            print('The answer is: ' + word)

    # if outcome == word:
        #print('You win!!')
        #print('The answer is: ' + word)
    # else:
       #print('You are completely hung :(')


def guess(dash, letter,word):
    for i in range(len(word)):
        print('You have ' + N_TURNS - i + ' wrong guesses left.')
        s = input('Your guess: ')
        include = replace(word, s, HIDE)
    print(str(include))
    word_looks_like = ans(word, s, HIDE)
    print('The word looks like: ' + str(word_looks_like))
    print('You have ' + N_TURNS + ' wrong guesses left.')


def replace(dash, letter):


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
