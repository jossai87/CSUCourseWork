'''
Program to print all 2-letter domain names.
Note that ord() and chr() convert between text and ASCII/ Unicode encodings.
ord('a') is 97. ord('b') is 98, and so on. chr(99) is 'c', etc.
'''
print('Two-letter domain names:')

import random

letter1 = 'a'
letter2 = '?'
ran_int = ''
while letter1 <= 'z':  # Outer loop
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop
        if ran_int == '1':
            print('{}{}.com'.format(letter1, ord(letter2)))
            ran_int = str(random.randint(1,2))
        else:
            print('{}{}.com'.format(letter1, letter2))
            ran_int = str(random.randint(1,2))
                  
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)

