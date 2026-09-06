# File Name:       day_16/part_2.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 16 Part 2 (https://adventofcode.com/2015/day/16)
# Last Updated:    21 Jan 2023

sues = []
with open("input.txt", "r") as file:
    for line in file:
        sue = {}
        line = line.strip("\n").split()
        for i in range(2, len(line), 2):
            sue[line[i].strip(":")] = int(line[i+1].strip(","))
        sues.append(sue)

for i, sue in enumerate(sues):
    found = ("children" not in sue or sue["children"] == 3)
    found = found and ("cats" not in sue or sue["cats"] > 7)
    found = found and ("samoyeds" not in sue or sue["samoyeds"] == 2)
    found = found and ("pomeranians" not in sue or sue["pomeranians"] < 3)
    found = found and ("akitas" not in sue or sue["akitas"] == 0)
    found = found and ("vizslas" not in sue or sue["vizslas"] == 0)
    found = found and ("goldfish" not in sue or sue["goldfish"] < 5)
    found = found and ("trees" not in sue or sue["trees"] > 3)
    found = found and ("cars" not in sue or sue["cars"] == 2)
    found = found and ("perfumes" not in sue or sue["perfumes"] == 1)
    if found:
        print(i+1)
        break
