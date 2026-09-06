# File Name:       day_14/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 14 Part 1 (https://adventofcode.com/2015/day/14)
# Last Updated:    21 Jan 2023

reindeers = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.split(" ")
        reindeers.append((int(line[3]), int(line[6]), int(line[-2])))

def race(reindeer, seconds):
    d = 0
    cycles = seconds // (reindeer[1]+reindeer[2])
    d += cycles * reindeer[1] * reindeer[0]
    frac = seconds % (reindeer[1]+reindeer[2])
    d += min(frac, reindeer[1]) * reindeer[0]
    return d

time = 2503
max_dist = 0
for reindeer in reindeers:
    max_dist = max(max_dist, race(reindeer, time))

print(max_dist)
