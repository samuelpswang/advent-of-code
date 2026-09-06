# File Name:       day_19/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 19 Part 1 (https://adventofcode.com/2015/day/19)
# Last Updated:    21 Jan 2023

# read input
replacements = {}
start = ""
with open("input.txt") as file:
    for line in file:
        line = line.strip("\n")
        if "=>" in line:
            line = line.split(" => ")
            if line[0] in replacements:
                replacements[line[0]].append(line[1])
            else:
                replacements[line[0]] = [line[1]]
        elif line != "":
            start = line
        else:
            continue

# function to replace one-by-one
def replace(source, key, values):
    results = []
    start = source.find(key)
    while start != -1:
        for value in values:
            result = source[:start] + value + source[start+len(key):]
            results.append(result)
        start = source.find(key, start+len(key))
    return results

# find one step solutions
one_steps = set()
for key, values in replacements.items():
    for result in replace(start, key, values):
        one_steps.add(result)

print(len(one_steps))
