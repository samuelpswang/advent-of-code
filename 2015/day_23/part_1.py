# File Name:       day_23/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 23 Part 1 (https://adventofcode.com/2015/day/23)
# Last Updated:    21 Jan 2023

instructions = []
with open("input.txt") as file:
    for line in file:
        line = line.strip("\n").split()
        if len(line) == 2:
            if line[0] == "jmp":
                instructions.append((line[0], "", int(line[1])))
            else:
                instructions.append((line[0], line[1], 0))
        else:
            line[1] = line[1].strip(",")
            instructions.append((line[0], line[1], int(line[2])))

regfile = { "a": 0, "b": 0 }
pc = 0
while pc < len(instructions):
    opc, reg, val = instructions[pc]
    match opc:
        case "hlf":
            regfile[reg] /= 2
            pc += 1
        case "tpl":
            regfile[reg] *= 3
            pc += 1
        case "inc":
            regfile[reg] += 1
            pc += 1
        case "jmp":
            pc += val
        case "jie":
            if regfile[reg] % 2 == 0:
                pc += val
            else:
                pc += 1
        case "jio":
            if regfile[reg] == 1:
                pc += val
            else:
                pc += 1

print(regfile["b"])
