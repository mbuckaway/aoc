# Problem 1

import os
import pathlib

# Checks if the required fields are available
def isvalid(fields):
    required = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    ]
    valid = True
    for check in required:
        if not check in fields:
            valid = False
            break
    #print("Isvalid: {}".format(valid))
    return valid


def main():
    filename = os.path.join(pathlib.Path(__file__).parent.absolute(),"input.txt")
    validpassports = 0
    records = 0
    with open(filename) as file:
        fields = dict()
        for line in file:
            line = line.strip("\n")
            #print(line)
            # If we have an empty line, we have a full record to process
            if line == '':
                if isvalid(fields):
                    validpassports+=1
                fields.clear()
                records+=1
                continue
            # Split the line by spaces to get the fields
            data = line.split(' ')
            # now, loop thru each item to get the keys/data
            for dataitem in data:
                [key, value] = dataitem.split(":")
                fields[key] = value
        # End of file, we need to do one last check
        if isvalid(fields):
            validpassports+=1
    print("We have {} valid passports of {} records".format(validpassports, records))
    # 215 too low

if __name__ == '__main__':
    main()
