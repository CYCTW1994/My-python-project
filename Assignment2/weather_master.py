"""
File: weather_master.py
Name: Cara
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""
EXIT = -100
COLD = -16


def main():
    print('stanCode \"Weather Master 4.0\"!')
    """
	check the value everytime whenever the user type in => compare high/low,
	calculate average and cold days => print
	"""
    max = -10000000
    min = 1000000
    ttl = 0
    count = 0
    cold = 0
    while True:
        data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
        if data == EXIT:
            print('No temperatures were entered.')
            break
        if data > max:
            max = data
        if data < min:
            min = data
        ttl += data
        count += 1
        avg = ttl / count
        if data < COLD:
            cold += 1
    print('Highest temperature = ' + str(max))
    print('Lowest temperature = ' + str(min))
    print('Average = ' + str(avg))
    print(str(cold) + ' cold day(s)')


# start to show highest/lowest/average temperature and cold day warning


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
