# File Name:       day_12/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 12 Part 1 (https://adventofcode.com/2015/day/12)
# Last Updated:    21 Jan 2023

import json

obj = []
with open("input.txt", "r") as file:
    obj = json.load(file)

total = 0
queue = [obj]
while queue: 
    curr = queue.pop()
    if type(curr) == dict:
        for key, item in curr.items():
            queue.append(item)
    elif type(curr) == list:
        for item in curr:
            queue.append(item)
    elif type(curr) == int:
        total += curr

print(total)
