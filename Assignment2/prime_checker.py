"""
File: prime_checker.py
Name:
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
from unittest.test.test_result import m

EXIT = -100


def main():
	"""
	if number is EXIT, then exit, if not, then go to check if it is a prime.
	"""
	print('Welcome to the prime checker!')
	n = int(input('n: '))
	while n != EXIT:
		if_prime(n)
		n = int(input('n: '))
	print('Have a good one!')


def if_prime(n):
	"""
	a prime is only available to be divided by 1 and itself
	"""
	for i in range(2, n):
		if n % i == 0:
			print(str(n) + ' is not a prime number.')
			return
	print(str(n) + ' is a prime number.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
