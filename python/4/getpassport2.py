# Problem 2

import os
import pathlib
import re

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

# Checks if the data in the fields is valid
def isvaliddata(fields):
    descriptors = {
        'byr':
            {
                'type': 'range',
                'regex':'^(\d\d\d\d)$',
                'min': 1920,
                'max': 2002
            },
        'iyr':
            {
                'type': 'range',
                'regex':'^(\d\d\d\d)$',
                'min': 2010,
                'max': 2020,
            },
        'eyr':
            {
                'type': 'range',
                'regex':'^(\d\d\d\d)$',
                'min': 2020,
                'max': 2030
            },
        'hgt':{
                'type': 'height',
                'regex':'^(\d+)(cm|in)$',
                'mincm': 150,
                'maxcm': 193,
                'minin': 59,
                'maxin': 76
            },
        'hcl':
            {
                'type': 'regex',
                'regex':'^(#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f])$'
            },
        'ecl':
            {
                'type': 'regex',
                'regex':'^(amb|blu|brn|gry|grn|hzl|oth)$'
            },
        'pid':
            {
                'type': 'regex',
                'regex':'^(\d\d\d\d\d\d\d\d\d)$'
            },
        'cid':
            {
                'type': 'ignore'
            }
    }
    valid = True
    # Validate the fields
    for field in fields:
        # Invalid field - give up
        if not field in descriptors:
            valid = False
            break
        descriptor = descriptors[field]
        # If only python supported case statements....
        if descriptor['type'] == 'range':
            regex = re.compile(descriptor['regex'])
            # Regex matches, check the numbers
            value = fields[field]
            if regex.match(value):
                intvalue = int(value)
                if intvalue < descriptor['min']:
                    valid = False
                    break
                if intvalue > descriptor['max']:
                    valid = False
                    break
            else:
                valid = False
        elif descriptor['type'] == 'height':
            regex = re.compile(descriptor['regex'])
            # Regex matches, check the numbers
            matched = regex.match(fields[field])
            if matched:
                groups = matched.groups()
                num = int(groups[0])
                unit = groups[1]
                if unit == 'cm':
                    if num > descriptor['maxcm'] or num < descriptor['mincm']:
                        valid = False
                        break
                else:
                    if num > descriptor['maxin'] or num < descriptor['minin']:
                        valid = False
                        break
            else:
                    valid = False
                    break
        elif descriptor['type'] == 'regex':
            regex = re.compile(descriptor['regex'])
            if not regex.match(fields[field]):
                valid = False
                break
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
                if isvalid(fields) and isvaliddata(fields):
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
        if isvalid(fields) and isvaliddata(fields):
            validpassports+=1
    print("We have {} valid passports with valid data of {} records".format(validpassports, records))

if __name__ == '__main__':
    main()
