import fs from "fs"

let input
input = fs.readFileSync("input.txt", { encoding: "utf8", flag: "r" })
input = input.split(", ")

let start = [0, 0]
let facing = 0 // 0: north, 1: east, 2: south, 3: west
let dx = [0, 1, 0, -1]
let dy = [1, 0, -1, 0]
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
    start[0] += dx[facing] * len
    start[1] += dy[facing] * len
}

console.log(Math.abs(start[0]) + Math.abs(start[1]))
