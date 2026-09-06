# File Name:       day_01/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 1 Part 1 (https://adventofcode.com/2015/day/1)
# Last Updated:    21 Jan 2023

floor = 0

with open("input.txt") as file:
    for ch in file.readline():
        if ch == '(':
            floor += 1
        else:
            floor -= 1

print(floor)
