# Problem 2
# Specifically, they need you to find the THREE entries that sum to 2020 and then multiply those THREE numbers together.
# For example, suppose your expense report contained the following:
# 1721
# 979
# 366
# 299
# 675
# 1456
# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.
# In your expense report, what is the product of the three entries that sum to 2020?

import os
import array
import pathlib
import time

start_time = time.time()

filename = os.path.join(pathlib.Path(__file__).parent.absolute(), "input.txt")
values = list()
with open(filename) as file:
    for line in file:
        values.append(int(line))
values = sorted(values)

maxlen = len(values)
value1 = 0
value2 = 0
value3 = 0
finished = False
# The long, ugly, and brute force method
for fromstart in range(0, maxlen):
    if finished:
        break
    for middle in range(0, maxlen):
        if finished:
            break
        for fromend in range(maxlen-1, 0, -1):
            value1 = values[fromstart]
            value2 = values[fromend]
            value3 = values[middle]
            if (value1+value2+value3==2020):
                print("Found it: {}+{}+{}={}".format(value1, value2, value3, value1+value2+value3))
                finished = True
                break

print("{}*{}*{}={}".format(value1, value2, value3, value1*value2*value3))

print("--- %s seconds ---" % (time.time() - start_time))

# Typical execution time is --- 0.0021719932556152344 seconds ---
