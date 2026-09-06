import fs from "fs"

let input
input = fs.readFileSync("input.txt", { encoding: "utf8", flag: "r" })
input = input.split("\n")

let input_t = []
for (let i = 0; i < input[0].length; i += 1) {
    let row = ""
    for (let line of input) {
        row += line[i]
    }
    input_t.push(row)
}

function getModeLetter(str) {
    let histogram = {}
    for (let c of str) {
        if (histogram[c] === undefined) histogram[c] = 1
        else histogram[c] += 1
    }
    
    let min_count = input_t[0].length, min_letter
    for (let key in histogram) {
        if (histogram[key] < min_count) {
            min_count = histogram[key]
            min_letter = key
        }
    }
    
    return min_letter
}

let message = input_t.map(getModeLetter).reduce((comb, c) => { return comb+c }, "")

console.log(message)
