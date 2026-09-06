# File Name:       day_01/part_2.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 1 Part 2 (https://adventofcode.com/2015/day/1)
# Last Updated:    21 Jan 2023

floor = 0
count = 0

with open("input.txt") as file:
    for i, ch in enumerate(file.readline()):
        if ch == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            count = i+1
            break
            
print(count)
