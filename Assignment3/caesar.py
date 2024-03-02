"""
File: caesar.py
Name: Cara
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    define new alphabet string (use "replace")
    => find 2 letters in the same index in normal alphabet string(A~Z) and new alphabet string(W~D)
    """
    secret_n = int(input('Secret number: '))
    s = input("What's the ciphered string? ")
    s = s.upper()
    if secret_n == 0:
        print('The deciphered string is: ' + str(s))
    else:
        new_alphabet = replace(ALPHABET, secret_n)  # new alphabet string after deciphering
        new = find_and_change(ALPHABET, new_alphabet, s)
        print('The deciphered string is: ' + str(new))


def replace(a_to_z, secret_number):
    """
    to make a new alphabet string (W~D)
    """
    ans = ''
    i = 26 - secret_number % 26
    # if secret number is 4 which means 'w'(i=22) will be the first letter(i=0)
    # if secret number is bigger than 26, than the actual secret number is remainder
    ans += a_to_z[i:]
    ans += a_to_z[:i]
    return ans


def find_and_change(a_to_z, new_alphabet, s):
    """
    find WLLHA and change their location
    """
    ans = ''
    for i in range(len(s)):
        i = new_alphabet.find(s[i])  # find s's index in new_alphabet
        ans += a_to_z[i:i+1]
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
