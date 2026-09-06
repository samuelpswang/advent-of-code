# File Name:       day_17/part_2.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 17 Part 2 (https://adventofcode.com/2015/day/17)
# Last Updated:    21 Jan 2023

# read input
containers = []
with open("input.txt") as file:
    for line in file:
        containers.append(int(line.strip("\n")))

# check characteristics
containers_count = {}
duplicates = set()
for container in containers:
    if container not in containers_count:
        containers_count[container] = 1
    else:
        containers_count[container] += 1
        duplicates.add(container)
assert(all(count <= 2 for count in [_ for cont, _ in containers_count.items()]))

# find solution
solutions = {0: set()}
solutions[0].add(())
def dp(target):
    # base case
    if target in solutions:
        return solutions[target]
    # recursion
    results = set()
    for cont in containers:
        if cont > target:
            continue
        combs = dp(target-cont)
        for comb in combs:
            if (cont in duplicates and comb.count(cont) < 2) or (cont not in duplicates and cont not in comb):
                curr = [*comb, cont]
                curr.sort()
                results.add((*curr,))
    solutions[target] = results
    return results
dp(150)

# count with min container count
count = 0
min_container_count = min(len(comb) for comb in solutions[150])
for comb in solutions[150]:
    if len(comb) != min_container_count:
        continue
    duplicates_count = 0
    for dup in duplicates:
        duplicates_count += (comb.count(dup) == 1)
    count += 2 ** duplicates_count
    
print(count)
