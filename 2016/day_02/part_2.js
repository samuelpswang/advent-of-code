import fs from "fs"

let input
input = fs.readFileSync("input.txt", { encoding: "utf8", flag: "r" })
input = input.split("\n")

const keypad = ["xx1xx", "x234x", "56789", "xABCx", "xxDxx"]
function getKeypad(location) { return keypad[location[0]][location[1]] }

const dr = { 'L': 0, 'R': 0, 'U': -1, 'D': 1 }
const dc = { 'L': -1, 'R': 1, 'U': 0, 'D': 0 }
function moveLocation(location, instruction) {
    let prev = [...location]
    location[0] += dr[instruction]
    location[1] += dc[instruction]
    if (location[0] < 0) location[0] = 0
    if (location[0] > 4) location[0] = 4
    if (location[1] < 0) location[1] = 0
    if (location[1] > 4) location[1] = 4
    if (getKeypad(location) === "x") {
        location[0] = prev[0]
        location[1] = prev[1]
    }
}

let code = ""
let start = [2, 0]
for (let instruction of input) {
    for (let subinstruction of instruction) {
        moveLocation(start, subinstruction)
    }
    code += getKeypad(start)
}

console.log(code)
