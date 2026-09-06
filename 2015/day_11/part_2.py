# File Name:       day_11/part_2.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 11 Part 2 (https://adventofcode.com/2015/day/11)
# Last Updated:    21 Jan 2023

from itertools import groupby

def inc(c):
    assert len(c) == 1
    if c == 'z': return 'a'
    else: return chr((ord(c)+1))

def increment(pwd):
    st = -1
    for i in range(len(pwd)-1, -1, -1):
        if pwd[i] != 'z':
            st = i
            break
    new_pwd = pwd[:st] + inc(pwd[st]) + 'a' * (len(pwd)-1-st)
    return new_pwd

def straight(st):
    if 'a' <= st <= 'x': return st + inc(st) + inc(inc(st))
    else: return ""

def is_valid_1(pwd):
    for i in range(len(pwd)-3):
        if pwd[i:i+3] == straight(pwd[i]):
            return True
    return False

def is_valid_2(pwd):
    return 'i' not in pwd and 'o' not in pwd and 'l' not in pwd

def is_valid_3(pwd):
    count = 0
    for key, group in groupby(pwd):
        if len(list(group)) >= 2:
            count += 1
        if count == 2:
            return True
    return False

def is_valid(pwd):
    return is_valid_1(pwd) and is_valid_2(pwd) and is_valid_3(pwd)


pwd = ""
with open("input.txt", "r") as file:
    for line in file:
        pwd = line.strip("\n")

while not is_valid(pwd):
    pwd = increment(pwd)

pwd = increment(pwd)

while not is_valid(pwd):
    pwd = increment(pwd)
    
print(pwd)
    