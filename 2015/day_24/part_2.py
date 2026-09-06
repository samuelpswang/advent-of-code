# File Name:       day_24/part_2.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 24 Part 2 (https://adventofcode.com/2015/day/24)
# Last Updated:    21 Jan 2023

from itertools import combinations
from math import prod

# read input
parcels = []
with open("input.txt") as file:
    for line in file:
        parcels.append(int(line.strip("\n")))
parcels.sort()
target = sum(parcels)/4

# finding mininum and maximum count to add up to target
min_count = max_count = 0
total = 0
count = 0
for i in range(len(parcels)):
    total += parcels[i]
    count += 1
    if total >= target:
        max_count = count
        break
total = 0
count = 0
for i in range(len(parcels)-1,-1,-1):
    total += parcels[i]
    count += 1
    if total >= target:
        min_count = count
        break

# find combinations
solutions = []
for size in range(min_count, max_count+1, 1):
    combs = [_ for _ in combinations(parcels, size)]
    for comb in combs:
        if sum(comb) == target:
            solutions.append(comb)
    if len(solutions) > 0:
        break

# find minimum product
min_prod = float("inf")
for comb in solutions:
    if prod(comb) < min_prod:
        min_prod = prod(comb)

print(min_prod)
