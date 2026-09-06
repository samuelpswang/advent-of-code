import { reverse } from "dns"
import fs from "fs"

const sectorIdRegex = /[0-9]+/
const checksumRegex = /\[[a-z]+\]/
const encryptedNameRegex = /[\w-]+\[/

function parseLine(line) {
    let name = line.match(encryptedNameRegex)[0].slice(0,-1)
    let id = Number(line.match(sectorIdRegex)[0])
    let checksum = line.match(checksumRegex)[0].slice(1,-1)
    return [name, id, checksum]
}

let input
input = fs.readFileSync("input.txt", { encoding: "utf8", flag: "r" })
input = input.split("\n")
input = input.map((line) => { return parseLine(line) })

function rotateChar(chr, val) {
    let seq 
    seq = chr.charCodeAt(0) - "a".charCodeAt(0)
    seq += val
    seq %= 26
    seq += "a".charCodeAt(0)
    return String.fromCharCode(seq)
}

function decodeWord(word, val) {
    let decoded = ""
    for (let c of word) {
        decoded += rotateChar(c, val)
    }
    return decoded
}

function decodeLine([name, id, checksum]) {
    let words = name.split("-")
    words.pop()
    words = words.map((word) => { return decodeWord(word, id) })
    return words
}

for (let line of input) {
    let words = (decodeLine(line))
    let message = ""
    for (let word of words) {
        message += word
    }
    if (message.match("northpoleobjects"))
        console.log(line[1])
}
