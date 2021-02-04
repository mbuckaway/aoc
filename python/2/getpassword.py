# Problem 1
# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
# For example, suppose your expense report contained the following:
# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

import os
import pathlib

validpass = 0

def testPassword(line):
    valid = False
    [rule, password] = line.split(':')
    password=password.strip()
    [rule, char] = rule.split()
    [min, max] = rule.split('-')
    count=password.count(char)
    if (count>=int(min) and count<=int(max)):
        valid = True
    return valid

filename = os.path.join(pathlib.Path(__file__).parent.absolute(),"input.txt")
with open(filename) as file:
    for line in file:
        if testPassword(line.strip(" \n")):
            validpass+=1

print("Found {} valid passwords".format(validpass))