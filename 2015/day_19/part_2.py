# File Name:       day_19/part_2.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 19 Part 2 (https://adventofcode.com/2015/day/19)
# Last Updated:    21 Jan 2023

from random import shuffle

# read input
replacements = []
medicine = ""
with open("input.txt") as file:
    for line in file:
        line = line.strip("\n")
        if "=>" in line:
            line = line.split(" => ")
            replacements.append((line[1], line[0]))
        elif line != "":
            medicine = line
        else:
            continue

# randomly replace
# finding the right sequence is hard, randomly trying the sequence might be 
# faster; as pointed out by @mjpieters
steps = 0
prev_steps = 0
curr = medicine
while curr != "e":
    changed = False
    for k, v in replacements:
        if k in curr:
            curr = curr.replace(k, v, 1)
            steps += 1
            changed = True
    if not changed:
        steps = 0
        curr = medicine
        shuffle(replacements)

print(steps)
