# Problem 2
#Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. 
#(Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. 
# Other occurrences of the letter are irrelevant for the purposes of policy enforcement.


import os
import sys
import array
import pathlib

validpass = 0

def testPassword(line):
    valid = False
    [rule, password] = line.split(':')
    password=password.strip()
    [rule, char] = rule.split()
    [first, second] = rule.split('-')
    first=int(first)-1
    second=int(second)-1
    pwdlen = len(password)
    # Check for invalid indexes before checking for valid chars
    # first and second must be 0 or greater and must be less then the password len or risk array index error
    if (first>=0 and second>=0 and first<pwdlen and second<pwdlen):
        # We are supposed to have ONE and ONLY ONE char that matches. So conditions:
        # char1 and not char2 - true
        # not char1 and char2 - true
        # char1 and char2 - false
        # not char1 and not char1 - false 
        if ((password[first] == char) and not (password[second]==char)):
            valid = True
        if (not (password[first] == char) and (password[second]==char)):
            valid=True
    else:
        print("Error condition")
    #print("{} {},{} - {} = {} {} = {}".format(char, first, second, password, password[first], password[second], valid))
    return valid

filename = os.path.join(pathlib.Path(__file__).parent.absolute(),"input.txt")
with open(filename) as file:
    for line in file:
        if testPassword(line.strip(" \n")):
            validpass+=1

print("Found {} valid passwords".format(validpass))
