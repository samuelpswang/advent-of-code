import fs from "fs"

let input
input = fs.readFileSync("input.txt", { encoding: "utf8", flag: "r" })
input = input.split(", ")

function record(visited, start) {
    if (visited.has(start.toString())) return true
    visited.add(start.toString())
    return false
}

function trace(start, end, facing) {
    let sd, ed, cc;
    let res = []
    switch (facing) {
        case 0:
            cc = end[0]
            sd = start[1]+1
            ed = end[1]
            for (let i = sd; i <= ed; i += 1) { res.push([cc, i].toString()) }
            break
        case 1:
            cc = end[1]
            sd = start[0]+1
            ed = end[0]
            for (let i = sd; i <= ed; i += 1) { res.push([i, cc].toString()) }
            break
        case 2:
            cc = end[0]
            sd = end[1]
            ed = start[1]-1
            for (let i = sd; i <= ed; i += 1) { res.push([cc, i].toString()) }
            break
        case 3:
            cc = end[1]
            sd = end[0]
            ed = start[0]-1
            for (let i = sd; i <= ed; i += 1) { res.push([i, cc].toString()) }
            break
    }
    return res
}

let start = [0, 0]
let facing = 0 // 0: north, 1: east, 2: south, 3: west
let dx = [0, 1, 0, -1]
let dy = [1, 0, -1, 0]
let visited = new Set()
let hq = null
for (let ins of input) {
    let len
    if (ins[0] == 'L') {
        facing += 3
        len = Number(ins.split('L')[1])
    } else {
        facing += 1
        len = Number(ins.split('R')[1])
    }
    facing %= 4

    let prev = [...start]
    start[0] += dx[facing] * len
    start[1] += dy[facing] * len

    let path = trace(prev, start, facing)
    for (let coord of path) {
        if (record(visited, coord)) hq = coord
    }

    if (hq) break;
}

hq = hq.split(',')
console.log(Math.abs(Number(hq[0])) + Math.abs(Number(hq[1])))
