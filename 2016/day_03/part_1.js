import fs from "fs"

function parseLineToVal(line) {
    let num = ["", "", ""]
    for (let i = 0; i < 3; i += 1) {
        line = line.trim()
        for (let c of line) {
            if (c === " ") break
            num[i] += c
            line = line.slice(1)
        }
    }
    num = num.map((str) => { return Number(str) })
    return num
}

let input
input = fs.readFileSync("input.txt", { encoding: "utf8", flag: "r" })
input = input.split("\n")
input = input.map((line) => { return parseLineToVal(line) })

let count = 0
for (let trig of input) {
    let sum = trig.reduce((psum, val) => { return psum + val }, 0)
    let min = Math.min(...trig)
    let max = Math.max(...trig)
    let mid = sum - max - min
    if ((min + mid) > max) count += 1
}

console.log(count)
