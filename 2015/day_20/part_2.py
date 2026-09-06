# File Name:       day_20/part_2.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 20 Part 2 (https://adventofcode.com/2015/day/20)
# Last Updated:    21 Jan 2023

from sympy.ntheory import factorint, divisors

target = 0
with open("input.txt") as file:
    for line in file:
        target = int(line.strip("\n"))

def number_of_presents(num):
    limit = num/50
    return sum([d for d in divisors(num) if d >= limit]) * 11

house = 1
while number_of_presents(house) < target:
    house += 1

print(house)
