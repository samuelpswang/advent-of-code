import fs from "fs"

function extractInfo(line) {    
    function processExtract(extract) {
        const numberRegex = /[0-9]+/g
        function extractNumber(str) {
            return Number(str.match(numberRegex)[0])
        }
        
        let cleanup = {}
        cleanup.type = extract[0][0]
        cleanup.num = extractNumber(extract[0])
        return cleanup
    }
    const entityRegex = /((value)|(bot)|(output)) [0-9]+/g
    let extracts = [...line.matchAll(entityRegex)].map(processExtract)
    return extracts
}

let input
input = fs.readFileSync("input.txt", { encoding: "utf8", flag: "r" })
input = input.split("\n")
input = input.map(extractInfo)

// initialize machinery
let bots = {}, out = {}
for (let info of input) {
    if (info.length === 3) {
        let [bot, low, high] = info
        if (bots[bot.num] === undefined) {
            bots[bot.num] = { "low": low, "high": high, "input": [] }
        } else {
            bots[bot.num].low = low
            bots[bot.num].high = high
        }
        if (low.type === "o") out[low.num] = []
        if (high.type === "o") out[high.num] = []
    } else {
        let [chip, bot] = info
        if (bots[bot.num] === undefined) bots[bot.num] = { "low": undefined, "high": undefined, "input": [ chip.num ] }
        else bots[bot.num].input.push(chip.num)
    }
}

// process 
let found = false
while (!found) {
    for (let bid in bots) {
        if (bots[bid].input.length === 2) {
            // extract values
            let lower = Math.min(...bots[bid].input)
            let higher = Math.max(...bots[bid].input)
            bots[bid].input = []
            
            // check if found
            if (lower === 17 && higher === 61) {
                console.log(Number(bid))
                found = true
                break
            }
            
            // handle outputs
            if (bots[bid].low.type === 'b') bots[bots[bid].low.num].input.push(lower)
            else out[bots[bid].low.num].push(lower)
            if (bots[bid].high.type === 'b') bots[bots[bid].high.num].input.push(higher)
            else out[bots[bid].high.num].push(higher)
        }
    }
    
    if (found) break
}
