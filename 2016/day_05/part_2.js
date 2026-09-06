import fs from "fs"
import md5 from "md5"

let input
input = fs.readFileSync("input.txt", { encoding: "utf8", flag: "r" })
input = input.trim("\n")

let id = input
function hashIndex(index) {
    return md5(id+index.toString())
}

function isStartWithFiveZeros(message) {
    for (let i = 0; i < 5; i += 1) {
        if (message[i] !== "0") return false;
    }
    return true;
}

function replaceStringAtDigit(src, chr, digit) {
    let tar = ""
    for (let i = 0; i < 8; i += 1) {
        if (i === digit) tar += chr
        else tar += src[i]
    }
    return tar
}

function isAllFound(str) {
    return str.match("_") === null
}

let index = 0
let passcode = "________"
let filled = [false, false, false, false, false, false, false, false]

while (true) {
    let message = hashIndex(index)
    if (isStartWithFiveZeros(message) && "0" <= message[5] && message[5] <= "7") {
        if (!filled[Number(message[5])]) {
            passcode = replaceStringAtDigit(passcode, message[6], Number(message[5]))
            filled[Number(message[5])] = true
        }
    }
    index += 1
    if (isAllFound(passcode)) break
}

console.log(passcode)

