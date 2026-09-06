# File Name:       day_06/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 6 Part 1 (https://adventofcode.com/2015/day/6)
# Last Updated:    21 Jan 2023

instructions = []
with open("input.txt", "r") as file:
    for line in file:
        if "turn on" in line:
            start, end = line.strip("turn on").strip().split(" through ")
            [sr, sc] = [int(n) for n in start.split(",")]
            [er, ec] = [int(n) for n in end.split(",")]
            instructions.append(("on", sr, sc, er, ec))
        elif "turn off" in line:
            start, end = line.strip("turn off").strip().split(" through ")
            [sr, sc] = [int(n) for n in start.split(",")]
            [er, ec] = [int(n) for n in end.split(",")]
            instructions.append(("off", sr, sc, er, ec))
        elif "toggle" in line:
            start, end = line.strip("toggle").strip().split(" through ")
            [sr, sc] = [int(n) for n in start.split(",")]
            [er, ec] = [int(n) for n in end.split(",")]
            instructions.append(("", sr, sc, er, ec))

lights = [[False for _ in range(1000)] for _ in range(1000)]
for op, sr, sc, er, ec in instructions:
    if op == "on":
        for r in range(sr, er+1):
            for c in range(sc, ec+1):
                lights[r][c] = True
    elif op == "off":
        for r in range(sr, er+1):
            for c in range(sc, ec+1):
                lights[r][c] = False
    else:
        for r in range(sr, er+1):
            for c in range(sc, ec+1):
                lights[r][c] = not lights[r][c]

total = sum([sum(row) for row in lights])
print(total)
