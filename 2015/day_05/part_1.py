# File Name:       day_05/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 5 Part 1 (https://adventofcode.com/2015/day/5)
# Last Updated:    21 Jan 2023

def has_three_vowels(s):
    vowels = "aeiou"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count >= 3

def has_double(s):
    prev = '0'
    for ch in s:
        if prev == ch:
            return True
        prev = ch
    return False

def has_no_bad_set(s):
    return "ab" not in s and "cd" not in s and "pq" not in s and "xy" not in s

def is_nice(s):
    return has_three_vowels(s) and has_double(s) and has_no_bad_set(s)

count = 0
with open("input.txt", "r") as file: 
    for line in file:
        line = line.strip("\n")
        if is_nice(line):
            count += 1

print(count)
