# File Name:       day_04/part_2.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 4 Part 2 (https://adventofcode.com/2015/day/4)
# Last Updated:    21 Jan 2023

from hashlib import md5

def is_valid(key, num):
    hexhash = md5((key+str(num)).encode()).hexdigest()
    return all(hexhash[i] == '0' for i in range(6))

key = ""
with open("input.txt", "r") as file:
    key = file.readline()

num = 0
while not is_valid(key, num): 
    num += 1

print(num)
