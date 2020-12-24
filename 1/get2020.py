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
import sys
import array
import pathlib


filename = os.path.join(pathlib.Path(__file__).parent.absolute(),"input.txt")
values = list()
with open(filename) as file:
    for line in file:
        values.append(int(line))
values = sorted(values)

maxlen = len(values)
value1 = 0
value2 = 0
finished = False
for fromstart in range(0, maxlen):
    if finished:
        break
    for fromend in range(maxlen-1, 0, -1):
        value1 = values[fromstart]
        value2 = values[fromend]
        if (value1+value2==2020):
            print("Found it: {}+{}={}".format(value1, value2, value1+value2))
            finished = True
            break

print("{}*{}={}".format(value1, value2, value1*value2))
