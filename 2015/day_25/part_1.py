# File Name:       day_25/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 25 Part 1 (https://adventofcode.com/2015/day/25)
# Last Updated:    21 Jan 2023

# reading input
line = open("input.txt").readline()
line = line.split()
row = int(line[line.index("row")+1].strip(","))
col = int(line[line.index("column")+1].strip("."))

# calculating nth
nth = (1 + (row+col-2)) * (row+col-2) / 2 + col
nth %= 33554393
nth = int(nth)

# finding value
val = 20151125
for _ in range(nth-1):
    val *= 252533
    val %= 33554393

print(val)
