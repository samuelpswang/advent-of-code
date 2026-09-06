# File Name:       day_03/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 3 Part 1 (https://adventofcode.com/2015/day/3)
# Last Updated:    21 Jan 2023

x = 0
y = 0
vis = set()
vis.add((0, 0))

with open("input.txt", "r") as file:
    dir = file.readline()

for ch in dir:
    match ch:
        case '<':
            x -= 1
        case '>':
            x += 1
        case '^':
            y += 1
        case 'v':
            y -= 1
    vis.add((x, y))
    
print(len(vis))
