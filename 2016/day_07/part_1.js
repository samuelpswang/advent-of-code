import fs from "fs"

function processLine(line) {
    return line.match(/[a-z]+/g)
}

let input
input = fs.readFileSync("input.txt", { encoding: "utf8", flag: "r" })
input = input.split("\n")
input = input.map(processLine)

function hasXyyx(str) {
    for (let i = 0; i < str.length-3; i += 1) {
        if (str[i] !== str[i+1] && str[i] === str[i+3] && str[i+1] === str[i+2]) return true
    }
    return false
}

function supportTls(line) {
    let outsideBrackets = false, insideBrackets = false
    for (let i = 0; i < line.length; i += 2) {
        if (hasXyyx(line[i])) outsideBrackets = true
    }
    for (let i = 1; i < line.length; i += 2) {
        if (hasXyyx(line[i])) insideBrackets = true
    }
    return !insideBrackets & outsideBrackets
}

let count = 0
for (let line of input) {
    if (supportTls(line)) count += 1
}

console.log(count)
