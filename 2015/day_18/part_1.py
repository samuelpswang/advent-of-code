# File Name:       day_18/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 18 Part 1 (https://adventofcode.com/2015/day/18)
# Last Updated:    21 Jan 2023

# read input
grid = []
with open("input.txt") as file:
    for line in file:
        grid.append(line.strip("\n"))
assert(len(grid) == 100)
assert(all(len(row) == 100 for row in grid))

# neighbors
# 0 1 2
# 3 x 4
# 5 6 7
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

# next iteration function
def valid(r, c):
    return 0 <= r <= 99 and 0 <= c <= 99

def next(grid):
    new_grid = ["" for _ in range(100)]
    for row in range(100):
        for col in range(100):
            if grid[row][col] == "#":
                alive_count = 0
                for i in range(8):
                    if valid(row+dr[i], col+dc[i]) and grid[row+dr[i]][col+dc[i]] == "#":
                        alive_count += 1
                if alive_count == 2 or alive_count == 3:
                    new_grid[row] += "#"
                else:
                    new_grid[row] += "."
            else:
                alive_count = 0
                for i in range(8):
                    if valid(row+dr[i], col+dc[i]) and grid[row+dr[i]][col+dc[i]] == "#":
                        alive_count += 1
                if alive_count == 3:
                    new_grid[row] += "#"
                else:
                    new_grid[row] += "."
    return new_grid

# iterations function
def step(grid, count):
    for _ in range(count):
        grid = next(grid)
    return grid

# run
grid = step(grid, 100)
on_count = 0
for row in grid:
    on_count += row.count("#")
print(on_count)
