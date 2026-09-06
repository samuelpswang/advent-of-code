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

function getHistogram(name) {
    let histogram = {}
    for (let c of name) {
        if (c.match(/[0-9]|[-]/)) continue
        if (c in histogram) histogram[c] += 1
        else histogram[c] = 1
    }
    return histogram
}

function getChecksum(histogram) {
    let list = []
    for (let key in histogram) {
        list.push([histogram[key], key])
    }
    list.sort((it1, it2) => {
        if (it1[0] < it2[0]) return -1
        else if (it1[0] > it2[0]) return 1
        if (it1[1] > it2[1]) return -1
        else return 1
    })
    list.reverse()

    let checksum = ""
    for (let i = 0; i < 5; i += 1) {
        checksum += list[i][1]
    }
    return checksum
}

function validateLine([name, _, checksum]) {
    return getChecksum(getHistogram(name)) === checksum
}

console.log(input.reduce((idsum, line) => { return (validateLine(line) ? idsum+line[1] : idsum)}, 0))
