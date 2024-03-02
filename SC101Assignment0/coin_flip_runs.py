"""
File: coin_flip_runs.py
Name: Cara
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	TODO:
	"""
	print("Let's flip a coin!")
	num_run = int(input('Number of runs: '))
	new_ch = ""
	last_ch = ""
	flag = False
	count = 0
	ans = ""
	while True:  # uncertain number to run
		roll = r.randrange(0,2)
		if roll == 0:
			new_ch = "H"
		else:
			new_ch = "T"
		if new_ch != last_ch:
			flag = False
		else:
			if not flag:  # original: flag == True
				flag = True
				count += 1	 # 2 situations: when the letter changed / letter in sequence
		if count == num_run:
			break
		last_ch = new_ch  # to see if the letter is same as the former one
		ans += new_ch
	print(ans)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
