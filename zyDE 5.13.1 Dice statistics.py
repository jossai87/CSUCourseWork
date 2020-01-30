'''
Create a different version of the program that:

Calculates the number of times the sum of the randomly rolled dice equals 
each possible value from 2 to 12.

Repeatedly asks the user for the number of times to roll the dice, quitting only 
when the user-entered number is less than 1. Hint: Use a while loop that will execute 
as long as num_rolls is greater than 1.

Prints a histogram in which the total number of times the dice rolls equals each possible 
value is displayed by printing a character, such as *, that number of times. The following 
provides an example:

'''
import random

num_twos = 0
num_threes = 0
num_fours = 0
num_fives = 0
num_sixes = 0
num_sevens = 0
num_eights = 0
num_nines = 0
num_tens = 0
num_elevens = 0
num_twelves = 0

num_rolls = 2

while num_rolls > 1:
    num_rolls = int(input('Enter number of rolls:\n'))

    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2

        #Count number of sixes and sevens
        if roll_total == 2:
            num_twos = num_sixes + 1
        if roll_total == 3:
            num_threes = num_sevens + 1
        if roll_total == 4:
            num_fours = num_sevens + 1
        if roll_total == 5:
            num_fives = num_sevens + 1
        if roll_total == 6:
            num_sixes = num_sevens + 1
        if roll_total == 7:
            num_sevens = num_sevens + 1
        if roll_total == 8:
            num_eights = num_sevens + 1  
        if roll_total == 9:
            num_nines = num_sevens + 1  
        if roll_total == 10:
            num_tens = num_sevens + 1  
        if roll_total == 11:
            num_elevens = num_sevens + 1  
        if roll_total == 12:
            num_twelves = num_sevens + 1         
            


 
    print('\nDice roll statistics:')
    print('2s:', num_twos * '*')
    print('3s:', num_threes * '*')
    print('4s:', num_fours * '*')
    print('5s:', num_fives * '*')
    print('6s:', num_sixes * '*')
    print('7s:', num_sevens * '*')
    print('8s:', num_eights * '*')
    print('9s:', num_nines * '*')
    print('10s:', num_tens * '*')
    print('11s:', num_elevens * '*')
    print('12s:', num_twelves * '*')

else:
    print('Invalid number of rolls. Try again.')

