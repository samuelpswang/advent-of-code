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

let count = 0
let index = 0
let passcode = ""
while (true) {
    let message = hashIndex(index)
    if (isStartWithFiveZeros(message)) {
        passcode += message[5]
        count += 1
    }
    index += 1
    if (count === 8) break
}

console.log(passcode)
