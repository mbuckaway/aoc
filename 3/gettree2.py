# Problem 1
# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
#
# Simpliest way is to read on a line at a time, skipping the first line. We keep a counter of the right position. We increment that by 3 each line 
# we read in. If the counter is longer than the line len, "wrap around" buy dividing the position by the line len to find out where in the current line
# we actually are - this is better than building the line repeating in memory - we just fake it. We keep going until the end of the file. End of file?
# report tree count. A tree is found by the # symbol in the position we are interested in.

import os
import pathlib

def readtrees(filename, right, down):
    linecount = 0
    position = 0
    trees = 0
    skip = 0
    with open(filename) as file:
        for line in file:
            # Special case: Moving down by 1, skip the first line only.
            if down==1 and linecount==0:
                linecount+=1
                continue
            # Moving down by more than 1, we need to skip every down lines after the first time thru
            if down>1 and skip<down:
                linecount+=1
                skip+=1
                continue
            skip = 1
            line = line.strip(" \n")
            linelen = len(line)
            position=position+right
            curpos=position
            if position>=linelen:
                curpos=position%linelen
            if line[curpos] == "#":
                trees+=1
            linecount+=1
    print("We bashed into {} trees for [{}][{}]".format(trees, right, down))
    return trees

def main():
    slopes = [
        [1,1],
        [3,1],
        [5,1],
        [7,1],
        [1,2],
    ]
    product = 1
    filename = os.path.join(pathlib.Path(__file__).parent.absolute(),"input.txt")
    for slope in slopes:
        # Array stores whole numbers, and we need ints
        right = slope[0]
        down = slope[1]
        trees=readtrees(filename, right, down)
        if right==3 and down==1 and not trees==151:
            raise ValueError("You done goofed. Wrong number of trees for 3, 1")
        if trees:
            product*=trees
    print("The product of all the tree counts is {}".format(product))

if __name__ == '__main__':
    main()
