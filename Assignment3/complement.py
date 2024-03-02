"""
File: complement.py
Name: Cara
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    TODO:
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    "dna" is the process, and "ans" is the final outcome that need to return back to main.
    """
    ans = ""  # start with empty string
    if dna == '':
        return 'DNA strand is missing.'  # directly return the string back to main instead of print here
    else:
        for i in range(len(dna)):
            ch = dna[i]
            if ch == 'A':
                ans = ans + 'T'
            if ch == 'T':
                ans = ans + 'A'
            if ch == 'C':
                ans = ans + 'G'
            if ch == 'G':
                ans = ans + 'C'
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
