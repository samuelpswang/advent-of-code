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
    
    let max_count = 0, max_letter
    for (let key in histogram) {
        if (histogram[key] > max_count) {
            max_count = histogram[key]
            max_letter = key
        }
    }
    
    return max_letter
}

let message = input_t.map(getModeLetter).reduce((comb, c) => { return comb+c }, "")

console.log(message)
