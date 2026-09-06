# File Name:       day_02/part_2.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 2 Part 2 (https://adventofcode.com/2015/day/2)
# Last Updated:    21 Jan 2023

def ribbon_length(l, w, h):
    min_side = min(l+w, w+h, h+l)
    return l*w*h + 2*min_side

sum = 0
with open("input.txt", "r") as file: 
    for line in file:
        [l, w, h] = [int(_) for _ in line.split("x")]
        sum += ribbon_length(l, w, h)

print(sum)
