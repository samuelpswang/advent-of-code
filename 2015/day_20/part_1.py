# File Name:       day_20/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 20 Part 1 (https://adventofcode.com/2015/day/20)
# Last Updated:    21 Jan 2023

from sympy.ntheory import factorint

target = 0
with open("input.txt") as file:
    for line in file:
        target = int(line.strip("\n"))

def number_of_presents(num):
    total = 1
    factor = factorint(num)
    for base, exp in factor.items():
        curr = 0
        for i in range(0,exp+1):
            curr += base ** i
        total *= curr
    return total * 10

house = 1
while number_of_presents(house) < target:
    house += 1

print(house)
