# File Name:       day_08/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 8 Part 1 (https://adventofcode.com/2015/day/8)
# Last Updated:    21 Jan 2023

def count_literal_eval(literal):
    literal = literal[1:-1]
    count = 0
    stack = []
    for ch in literal:
        match ch:
            case "\\":
                if len(stack) > 0 and stack[-1] == "\\":
                    stack.pop()
                    count += 1
                else:
                    stack.append(ch)
            case "\"":
                if len(stack) > 0 and stack[-1] == "\\":
                    stack.pop()
                    count += 1
                else:
                    assert False
            case "x":
                if len(stack) > 0 and stack[-1] == "\\":
                    stack.append(ch)
                else:
                    count += 1
            case _:
                if len(stack) == 2 and stack[0] == "\\" and stack[1] == "x":
                    stack.append(ch)
                elif len(stack) == 3 and stack[0] == "\\" and stack[1] == "x":
                    stack.clear()
                    count += 1
                else:
                    count += 1
    return count

total = 0
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip('\n')
        rep = len(line)
        act = count_literal_eval(line)
        total += rep-act

print(total)

# as shown by @mjpieters, it is evidently easier to just use:
# from ast import literal_eval
# act = len(literal_eval(line))
# this method was used in checking my stack algorithm as well
