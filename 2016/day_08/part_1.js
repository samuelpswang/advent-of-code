import fs from "fs"

let input
input = fs.readFileSync("input.txt", { encoding: "utf8", flag: "r" })
input = input.split("\n")

function rectCommand([cs, rs], state) {
    for (let r = 0; r < rs; r += 1) {
        for (let c = 0; c < cs; c += 1) {
            state[r][c] = true
        }
    }
}

function rotateArray(array, by) {
    by %= array.length
    let newArray = []
    for (let i = 0; i < array.length; i += 1) {
        let pi = (i - by + array.length) % array.length
        newArray.push(array[pi])
    }
    return newArray
}

function rotateRowCommand([r, by], state) {
    let row = state[r]
    let newRow = rotateArray(row, by)
    state[r] = newRow
}

function rotateColCommand([c, by], state) {
    let col = []
    for (let r = 0; r < state.length; r += 1) {
        col.push(state[r][c])
    }
    let newCol = rotateArray(col, by)
    for (let r = 0; r < state.length; r += 1) {
        state[r][c] = newCol[r]
    }
}

const numberRegex = /[0-9]+/g
const rectCommandRegex = /rect/g
const rowCommandRegex = /row/g
const colCommandRegex = /column/g
function decodeCommand(state, line) {
    let val
    val = [...line.matchAll(numberRegex)]
    val = val.map((item) => Number(item[0]))
    if (line.match(rectCommandRegex)) {
        rectCommand(val, state)
    } else if (line.match(rowCommandRegex)) {
        rotateRowCommand(val, state)
    } else if (line.match(colCommandRegex)) {
        rotateColCommand(val, state)
    }
    return state
}

let state = []
let row = []
for (let _ = 0; _ < 50; _ += 1) { row.push(false) }
for (let _ = 0; _ < 6; _ += 1) { state.push([...row]) }

state = input.reduce(decodeCommand, state)

let count = 0
for (let r of state) {
    for (let c of r) {
        count += (c ? 1 : 0)
    }
}

console.log(count)
