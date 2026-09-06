# File Name:       day_21/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 21 Part 1 (https://adventofcode.com/2015/day/21)
# Last Updated:    21 Jan 2023

from gekko import GEKKO

# read boss stats
boss = (0, 0, 0)
with open("input.txt") as file:
    lines = [line.strip("\n") for line in file]
    lines = [line.split(":")[1] for line in lines]
    lines = [int(line.strip()) for line in lines]
    boss = (lines[0], lines[1], lines[2])

# initialize gekko
m = GEKKO()
m.options.SOLVER = 1

# Initialize variables
w1 = m.Var(lb=0, ub=1, integer=True)
w2 = m.Var(lb=0, ub=1, integer=True)
w3 = m.Var(lb=0, ub=1, integer=True)
w4 = m.Var(lb=0, ub=1, integer=True)
w5 = m.Var(lb=0, ub=1, integer=True)

a1 = m.Var(lb=0, ub=1, integer=True)
a2 = m.Var(lb=0, ub=1, integer=True)
a3 = m.Var(lb=0, ub=1, integer=True)
a4 = m.Var(lb=0, ub=1, integer=True)
a5 = m.Var(lb=0, ub=1, integer=True)

r1 = m.Var(lb=0, ub=1, integer=True)
r2 = m.Var(lb=0, ub=1, integer=True)
r3 = m.Var(lb=0, ub=1, integer=True)
r4 = m.Var(lb=0, ub=1, integer=True)
r5 = m.Var(lb=0, ub=1, integer=True)
r6 = m.Var(lb=0, ub=1, integer=True)

# minimize cost
m.Obj(w1 * 8 + w2 * 10 + w3 * 25 + w4 * 40 + w5 * 74 + \
      a1 * 13 + a2 * 31 + a3 * 53 + a4 * 75 + a5 * 102 + \
      r1 * 25 + r2 * 50 + r3 * 100 + r4 * 20 + r5 * 40 + r6 * 80)

# count constraint
m.Equation((w1 + w2 + w3 + w4 + w5) == 1)
m.Equation((a1 + a2 + a3 + a4 + a5) <= 1)
m.Equation((r1 + r2 + r3 + r4 + r5 + r6) <= 2)

# survival constraint
# boss_health / (your_damage - boss_armour) <= your_health / (boss_damage - your_armour)
boss_health, boss_damage, boss_armour = boss
your_health = 100
your_damage = w1 * 4 + w2 * 5 + w3 * 6 + w4 * 7 + w5 * 8 + r1 * 1 + r2 * 2 + r3 * 3
your_armour = a1 * 1 + a2 * 2 + a3 * 3 + a4 * 4 + a5 * 5 + r4 * 1 + r5 * 2 + r6 * 3
m.Equation(boss_health / (your_damage - boss_armour) <= your_health / (boss_damage - your_armour))

# solve
m.solve(disp=False)

print(int(m.options.objfcnval))
