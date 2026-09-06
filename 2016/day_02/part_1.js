import fs from "fs"

let input
input = fs.readFileSync("input.txt", { encoding: "utf8", flag: "r" })
input = input.split("\n")

const keypad = ["123", "456", "789"]
function getKeypad(row, col) { return keypad[row][col] }

const dr = { 'L': 0, 'R': 0, 'U': -1, 'D': 1 }
const dc = { 'L': -1, 'R': 1, 'U': 0, 'D': 0 }
function moveLocation(location, instruction) {
    location[0] += dr[instruction]
    location[1] += dc[instruction]
    if (location[0] < 0) location[0] = 0
    if (location[0] > 2) location[0] = 2
    if (location[1] < 0) location[1] = 0
    if (location[1] > 2) location[1] = 2
}

let code = ""
let start = [1,1]
for (let instruction of input) {
    for (let subinstruction of instruction) {
        moveLocation(start, subinstruction)
    }
    code += getKeypad(start[0], start[1])
}

console.log(code)
