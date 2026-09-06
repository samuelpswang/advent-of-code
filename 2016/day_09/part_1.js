import fs from "fs"

let input
input = fs.readFileSync("input.txt", { encoding: "utf8", flag: "r" })
input = input.split("\n")

const numberRegex = /[0-9]+/g
const markerRegex = /\([0-9]+x[0-9]+\)/g

function getMarkerVal(marker) {
    return [...marker.matchAll(numberRegex)].map((item) => { return Number(item[0]) })
}

function getDecodeLength(state, line) {
    // find potential markers and format data
    let potentialMarkers = 
        [...line.matchAll(markerRegex)]
        .map((item) => { return [...getMarkerVal(item[0]), item.index, item[0].length] })

    // find actual markers
    let actualMarkers = [], maxRange = 0
    for (let pmark of potentialMarkers) {
        let [dataLen, dataIter, markIndex, markLen] = pmark
        let nextStartIndex = markIndex + markLen + dataLen
        if (actualMarkers.length === 0 || markIndex >= maxRange) {
            maxRange = nextStartIndex
            actualMarkers.push([...pmark])
        }
    }

    // process
    let len = line.length
    for (let amark of actualMarkers) {
        let [dataLen, dataIter, markIndex, markLen] = amark
        len -= markLen
        len += dataLen * (dataIter - 1)
    }
    return state + len
}

let total = input.reduce(getDecodeLength, 0)

console.log(total)
