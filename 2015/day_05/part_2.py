# File Name:       day_05/part_2.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 5 Part 2 (https://adventofcode.com/2015/day/5)
# Last Updated:    21 Jan 2023

def has_two_pair(s):
    for i in range(len(s)-1):
        if s.find(s[i:i+2], i+2) != -1:
            return True
    return False

def has_sandwich(s):
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            return True
    return False

def is_nice(s):
    return has_two_pair(s) and has_sandwich(s)

count = 0
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        if is_nice(line):
            count += 1

print(count)
