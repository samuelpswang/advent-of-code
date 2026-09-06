# File Name:       day_14/part_2.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 14 Part 2 (https://adventofcode.com/2015/day/14)
# Last Updated:    21 Jan 2023

reindeers = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.split(" ")
        reindeers.append((int(line[3]), int(line[6]), int(line[-2])))

def race(reindeer, seconds):
    d = 0
    full = seconds // (reindeer[1]+reindeer[2])
    d += full * reindeer[0] * reindeer[1]
    frac = seconds % (reindeer[1]+reindeer[2])
    d += min(frac, reindeer[1]) * reindeer[0]
    return d

def lead(dists):
    assert type(dists) == list
    max_val = max(dists)
    max_ind = []
    for i, dist in enumerate(dists):
        if dist == max_val:
            max_ind.append(i)
    return max_ind

time = 2503
score = [0 for _ in range(len(reindeers))]
for seconds in range(1, time+1):
    dist = []
    for i, reindeer in enumerate(reindeers):
        dist.append(race(reindeer, seconds))
    for i in lead(dist):
        score[i] += 1

print(max(score))
