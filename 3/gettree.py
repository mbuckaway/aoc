# Problem 1
# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
#
# Simpliest way is to read on a line at a time, skipping the first line. We keep a counter of the right position. We increment that by 3 each line 
# we read in. If the counter is longer than the line len, "wrap around" buy dividing the position by the line len to find out where in the current line
# we actually are - this is better than building the line repeating in memory - we just fake it. We keep going until the end of the file. End of file?
# report tree count. A tree is found by the # symbol in the position we are interested in.

import os
import pathlib

def main():
    filename = os.path.join(pathlib.Path(__file__).parent.absolute(),"input.txt")
    linecount = 0
    position = 0
    trees = 0
    with open(filename) as file:
        for line in file:
            # Skip the first line, because we move right 3, 1 down. So, start on line 2
            if linecount==0:
                linecount+=1
                continue
            line = line.strip(" \n")
            #print(line)
            linelen = len(line)
            position=position+3
            curpos=position
            if position>=linelen:
                curpos=position%linelen
            #print("position={} curpos={} char={}".format(position, curpos,line[curpos]))
            if line[curpos] == "#":
                trees+=1
            linecount+=1
    print("We bashed into {} trees".format(trees))

if __name__ == '__main__':
    main()
