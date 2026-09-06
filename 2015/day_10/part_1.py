# File Name:       day_10/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 10 Part 1 (https://adventofcode.com/2015/day/10)
# Last Updated:    21 Jan 2023

iterations = 40

prompt = ""
with open("input.txt", "r") as file:
    for line in file:
        prompt = line.strip("\n")

count = -1
prev = -1
next_prompt = ""
for _ in range(iterations):
    for ch in prompt:
        if prev == -1:
            prev = int(ch)
            count = 1
        elif prev == int(ch):
            count += 1
        else:
            next_prompt += str(count) + str(prev)
            prev = int(ch)
            count = 1
    next_prompt += str(count) + str(prev)
    prompt = next_prompt
    next_prompt = ""
    count = -1
    prev = -1

print(len(prompt))
