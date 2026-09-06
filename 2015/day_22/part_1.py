# File Name:       day_22/part_1.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 22 Part 1 (https://adventofcode.com/2015/day/22)
# Last Updated:    21 Jan 2023

from heapq import heappush, heappop
from copy import deepcopy

# construct spell properties
spells = { # cost, rounds, d_your_mana, d_your_hp, d_your_dm, d_your_sh, d_boss_hp
    "m": (-53, 0, 0, 0, 0, 0, -4),
    "d": (-73, 0, 0, 2, 0, 0, -2),
    "s": (-113, 6, 0, 0, 0, 7, 0),
    "p": (-173, 6, 0, 0, 0, 0, -3),
    "r": (-229, 5, 101, 0, 0, 0, 0)
}

# read input
boss_hp = boss_dm = 0
with open("input.txt") as file:
    for i, line in enumerate(file):
        line = int(line.split(": ")[1].strip("\n"))
        if i == 0: boss_hp = line
        else: boss_dm = line

# state class to track status at the end of each 2 rounds
class State:
    def __init__(self):
        # your stats
        self.your_mana = 500
        self.your_hp = 50
        self.your_dm = 0
        self.your_sh = 0
        self.your_casted = {
            "m": -1,
            "d": -1,
            "s": -1, 
            "p": -1,
            "r": -1
        }
        # boss stats
        self.boss_hp = boss_hp
        self.boss_dm = boss_dm
        # general stat
        self.mana_spent = 0
        self.spell_cast = ""
        
    def __gt__(self, other): # only for priority queue, sort by lowest boss hp, to keep length of priority queue low
        return self.boss_hp > other.boss_hp
    
    def cast(self, spell):
        # your round
        # a) previous effects & check if terminate
        for prev_spell in spells:
            if self.your_casted[prev_spell] != -1:
                _, rounds, d_your_mana, d_your_hp, d_your_dm, d_your_sh, d_boss_hp = spells[prev_spell]
                self.your_mana += d_your_mana
                self.your_hp += d_your_hp
                self.your_dm += d_your_dm
                self.boss_hp += d_boss_hp
                if self.your_casted[prev_spell] == -1+rounds: # shields only boost once per cast
                    self.your_sh += d_your_sh
                self.your_casted[prev_spell] -= 1
            if self.your_casted["s"] == -1: # only one shield at a time, clear shield after timeout
                    self.your_sh = 0
        if self.your_hp <= 0 or self.boss_hp <= 0 or self.your_mana <= 0:
            return False
        
        # b) fetch details & cast
        cost, rounds, d_your_mana, d_your_hp, d_your_dm, d_your_sh, d_boss_hp = spells[spell]
        self.mana_spent -= cost
        self.spell_cast += spell
        self.your_mana += cost
        self.your_casted[spell] += rounds
        
        # c) apply immediate effects & check if terminate
        if rounds == 0:
            self.your_mana += d_your_mana
            self.your_hp += d_your_hp
            self.your_dm += d_your_dm
            self.your_sh += d_your_sh
            self.boss_hp += d_boss_hp
        if self.your_hp <= 0 or self.boss_hp <= 0 or self.your_mana <= 0:
            return False
        
        # boss round
        # a) previous effects & check if terminate
        for prev_spell in spells:
            if self.your_casted[prev_spell] != -1:
                _, rounds, d_your_mana, d_your_hp, d_your_dm, d_your_sh, d_boss_hp = spells[prev_spell]
                self.your_mana += d_your_mana
                self.your_hp += d_your_hp
                self.your_dm += d_your_dm
                self.boss_hp += d_boss_hp
                if self.your_casted[prev_spell] == -1+rounds: # same thing with shields
                    self.your_sh += d_your_sh
                self.your_casted[prev_spell] -= 1
            if self.your_casted["s"] == -1: # same thing with shields
                    self.your_sh = 0
        if self.your_hp <= 0 or self.boss_hp <= 0 or self.your_mana <= 0:
            return False
        
        # b) boss deals damage & check if terminate
        actual_dm = self.boss_dm - self.your_sh
        if actual_dm < 1:
            actual_dm = 1
        self.your_hp -= actual_dm
        if self.your_hp <= 0 or self.boss_hp <= 0 or self.your_mana <= 0:
            return False 
        
        return True
    
    def is_good_to_cast(self, spell):
        return self.your_casted[spell] <= 0
    
    def is_lost(self):
        return self.your_hp <= 0 or self.your_mana <= 0

    def is_won(self):
        return self.boss_hp <= 0


# depth first search
# on a m1 pro this takes about 60 seconds
pq = [State()]
solution = float("inf")
it = 0
while pq:
    top = heappop(pq)
    for spell in spells:
        top_cp = deepcopy(top)
        if not top_cp.is_good_to_cast(spell):
            continue
        
        result = top_cp.cast(spell)
        if not result and top_cp.is_won():
            solution = min(solution, top_cp.mana_spent)
        elif result and top_cp.mana_spent < solution:
            heappush(pq, top_cp)

print(solution)
