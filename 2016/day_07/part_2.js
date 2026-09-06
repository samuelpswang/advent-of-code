import fs from "fs"

function processLine(line) {
    return line.match(/[a-z]+/g)
}

let input
input = fs.readFileSync("input.txt", { encoding: "utf8", flag: "r" })
input = input.split("\n")
input = input.map(processLine)

function reverseXyx(str) {
    return str[1] + str[0] + str[1]
}

function findXyx(str) {
    let found = []
    for (let i = 0; i < str.length-2; i += 1) {
        if (str[i] !== str[i+1] && str[i] === str[i+2]) found.push(str.slice(i,i+3))
    }
    return found
}

function supportSSL(line) {
    let outsideBrackets = [], insideBrackets = []
    for (let i = 0; i < line.length; i += 2) {
        outsideBrackets = outsideBrackets.concat(findXyx(line[i]))
    }
    for (let i = 1; i < line.length; i += 2) {
        insideBrackets = insideBrackets.concat(findXyx(line[i]))
    }
    let insideBracketsR = insideBrackets.map(reverseXyx)
    let intersect = outsideBrackets.filter((item) => { return insideBracketsR.includes(item) })
    return (intersect.length > 0)
}

let count = 0
for (let line of input) {
    if (supportSSL(line)) count += 1
}

console.log(count)
