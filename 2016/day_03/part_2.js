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

let actual = []
for (let row = 0; row < input.length; row += 3) {
    for (let col = 0; col < 3; col += 1) {
        actual.push([input[row][col], input[row+1][col], input[row+2][col]])
    }
}

let count = 0
for (let trig of actual) {
    let sum = trig.reduce((psum, val) => { return psum + val }, 0)
    let min = Math.min(...trig)
    let max = Math.max(...trig)
    let mid = sum - max - min
    if ((min + mid) > max) count += 1
}

console.log(count)
