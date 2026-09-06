# File Name:       day_15/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 15 Part 1 (https://adventofcode.com/2015/day/15)
# Last Updated:    21 Jan 2023

from gekko import GEKKO

# read ingredients
ingredients = []
with open("input.txt", "r") as file:
    for line in file:
        _, line = line.strip("\n").split(": ")
        line = line.split(", ")
        line = [int(item.split()[1]) for item in line]
        ingredients.append(line)

# initialize gekko
m = GEKKO()
m.options.SOLVER = 1

# Initialize variables
x1 = m.Var(value=100, lb=0, ub=100, integer=True)
x2 = m.Var(value=0, lb=0, ub=100, integer=True)
x3 = m.Var(value=0, lb=0, ub=100, integer=True)
x4 = m.Var(value=0, lb=0, ub=100, integer=True)

# minimize objective function
m.Obj((x1 * ingredients[0][0] + x2 * ingredients[1][0] + x3 * ingredients[2][0] + x4 * ingredients[3][0]) * \
      (x1 * ingredients[0][1] + x2 * ingredients[1][1] + x3 * ingredients[2][1] + x4 * ingredients[3][1]) * \
      (x1 * ingredients[0][2] + x2 * ingredients[1][2] + x3 * ingredients[2][2] + x4 * ingredients[3][2]) * \
      (x1 * ingredients[0][3] + x2 * ingredients[1][3] + x3 * ingredients[2][3] + x4 * ingredients[3][3]) * (-1))

# constraints
m.Equation((x1 + x2 + x3 + x4) == 100)
m.Equation((x1 * ingredients[0][0] + x2 * ingredients[1][0] + x3 * ingredients[2][0] + x4 * ingredients[3][0]) >= 0)
m.Equation((x1 * ingredients[0][1] + x2 * ingredients[1][1] + x3 * ingredients[2][1] + x4 * ingredients[3][1]) >= 0)
m.Equation((x1 * ingredients[0][2] + x2 * ingredients[1][2] + x3 * ingredients[2][2] + x4 * ingredients[3][2]) >= 0)
m.Equation((x1 * ingredients[0][3] + x2 * ingredients[1][3] + x3 * ingredients[2][3] + x4 * ingredients[3][3]) >= 0)

# solve
m.solve(disp=False)

# print results
print(int(m.options.objfcnval) * (-1))

# this problem is a mixed-integer non-linear program, in which gekko is used
# to solve; note that the objective function was set to negative to imitate
# minimize instead of maximize
