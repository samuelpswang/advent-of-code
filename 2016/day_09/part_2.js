import fs from "fs"

let input
input = fs.readFileSync("input.txt", { encoding: "utf8", flag: "r" })
input = input.split("\n")

const numberRegex = /[0-9]+/g
const monadRegex = /([a-zA-Z])|(\([0-9]+x[0-9]+\))/g

function getMarkerVal(marker) {
    return [...marker.matchAll(numberRegex)].map((item) => { return Number(item[0]) })
}

function getDecodeQueue(line) {
    let queue = 
        [...line.matchAll(monadRegex)]
        .map((item) => { 
            if (item[0].length === 1) return [0, 0, item.index, 1]
            else return [...getMarkerVal(item[0]), item.index, item[0].length]
        })
    return queue
}

function getDecodeLength(queue) {
    let stack = [], total = 0
    for (let [dataLen, dataIter, itemIndex, itemLength] of queue) {
        if (stack.length === 0) {
            if (itemLength === 1) {
                total += 1
            } else {
                stack.push([dataLen, dataIter, itemLength, 0, 0])
            }
        } else {
            if (itemLength == 1) {
                stack[stack.length-1][3] += 1
                stack[stack.length-1][4] += 1
                while (stack[stack.length-1][0] === stack[stack.length-1][3]) {
                    let topCompressedLength = stack[stack.length-1][3] + stack[stack.length-1][2]
                    let topActualLength = stack[stack.length-1][4] * stack[stack.length-1][1]
                    stack.pop()
                    if (stack.length === 0) {
                        total += topActualLength
                        break
                    } else {
                        stack[stack.length-1][3] += topCompressedLength
                        stack[stack.length-1][4] += topActualLength
                    }
                }
            } else {
                stack.push([dataLen, dataIter, itemLength, 0, 0])
            }
        }
    }
    return total
}

function getLength(state, line) {
    return state + getDecodeLength(getDecodeQueue(line))
}

let total = input.reduce(getLength, 0)

console.log(total)
