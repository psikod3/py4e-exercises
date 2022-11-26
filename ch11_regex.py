""" In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers
in the file and compute the sum of the numbers.

Data Files We provide two files for this assignment. One is a sample file where we give you the sum for your testing
and the other is the actual data you need to process for the assignment."""

# py ch11_regex.py

import re
hand = open('regex_sum_1616379.txt')
numbers = []

for line in hand:
    str_numlist = re.findall("([0-9]+)", line)

    if len(str_numlist) == 0: 
        continue

    for index, number in enumerate(str_numlist):  # idiom
        numbers.append(int(number))
        
    '''for i in range(len(str_numlist)):
        number = int(str_numlist[i])
        numbers.append(number)'''
        
print(sum(numbers))
