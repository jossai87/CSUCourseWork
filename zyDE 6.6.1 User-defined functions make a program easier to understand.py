'''
The problem below uses the function get_numbers() to read a number of integers 
from the user. Three unfinished functions are defined, which should print only 
certain types of numbers that the user entered. Complete the unfinished functions, 
adding loops and branches where necessary. Match the output with the below sample:

Enter 5 integers:
0 5
1 99
2 -44
3 0
4 12
Numbers: 5 99 -44 0 12
Odd numbers: 5 99
Negative numbers: -44
'''

size = 5

def get_numbers(num):
    numbers = []
    user_input = input('Enter {} integers:\n'.format(num))

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    # Print numbers
    print('Numbers:' + str(numbers))

def print_odd_numbers(numbers):
    # Print all odd numbers
    num_list = []
    for num in numbers:
        if num % 2 != 0:
            num_list.append(num)
    print('Odd numbers:' + ''.join(str(num_list)))


def print_negative_numbers(numbers):
    # Print all negative numbers
    num_list = []
    for num in numbers:
        if num < 0:
            num_list.append(num)
    print('Negative numbers:' + ''.join(str(num_list)))

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)