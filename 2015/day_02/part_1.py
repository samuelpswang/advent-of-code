# File Name:       day_02/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 2 Part 1 (https://adventofcode.com/2015/day/2)
# Last Updated:    21 Jan 2023

def wrapping_paper_area(l, w, h):
    min_side = min(l*w, w*h, h*l)
    return 2*l*w + 2*w*h + 2*h*l + min_side

sum = 0
with open("input.txt", "r") as file:
    for line in file:
        [l, w, h] = [int(_) for _ in line.split("x")]
        sum += wrapping_paper_area(l, w, h)

print(sum)
