# File Name:       day_07/part_2.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 7 Part 2 (https://adventofcode.com/2015/day/7)
# Last Updated:    21 Jan 2023

previous_a = 956
queue = []
wires = { 'b': previous_a }

def is_num(op):
    try:
        num = int(op)
        return True
    except ValueError:
        return False

def val(op):
    if is_num(op):
        return int(op)
    else:
        return wires[op]

with open("input.txt", "r") as file:
    for line in file:
        [sig, out] = [_.strip() for _ in line.split(" -> ")]
        if "NOT" in sig:
            ops = [sig.strip("NOT").strip()]
            if all(op in wires or is_num(op) for op in ops):
                wires[out] = (~val(ops[0])) & 65535
            else:
                queue.append(("NOT", ops, out))
        elif "AND" in sig:
            ops = [_.strip() for _ in sig.split("AND")]
            if all(op in wires or is_num(op) for op in ops):
                wires[out] = (val(ops[0]) & val(ops[1])) & 65535
            else:
                queue.append(("AND", ops, out))
        elif "OR" in sig:
            ops = [_.strip() for _ in sig.split("OR")]
            if all(op in wires or is_num(op) for op in ops):
                wires[out] = (val(ops[0]) | val(ops[1])) & 65535
            else:
                queue.append(("OR", ops, out))
        elif "LSHIFT" in sig:
            ops = [_.strip() for _ in sig.split("LSHIFT")]
            if all(op in wires or is_num(op) for op in ops):
                wires[out] = (val(ops[0]) << val(ops[1])) & 65535
            else:
                queue.append(("LSHIFT", ops, out))
        elif "RSHIFT" in sig:
            ops = [_.strip() for _ in sig.split("RSHIFT")]
            if all(op in wires or is_num(op) for op in ops):
                wires[out] = (val(ops[0]) >> val(ops[1])) & 65535
            else:
                queue.append(("RSHIFT", ops, out))
        elif is_num(sig):
            wires[out] = int(sig)
        else:
            queue.append(("", [sig], out))
        wires['b'] = previous_a

while queue:
    opt, ops, out = queue.pop(0)
    if all(op in wires or is_num(op) for op in ops):
        match opt:
            case "NOT":
                wires[out] = (~val(ops[0])) & 65535
            case "AND":
                wires[out] = (val(ops[0]) & val(ops[1])) & 65535
            case "OR":
                wires[out] = (val(ops[0]) | val(ops[1])) & 65535
            case "LSHIFT":
                wires[out] = (val(ops[0]) << val(ops[1])) & 65535
            case "RSHIFT":
                wires[out] = (val(ops[0]) >> val(ops[1])) & 65535
            case "":
                wires[out] = val(ops[0])
    else:
        queue.append((opt, ops, out))
    wires['b'] = previous_a

print(wires['a'])
