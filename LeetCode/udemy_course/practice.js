function stringsToNumbers(arr) {
    if (arr == null || arr == undefined) return []
    return arr.map(x => parseInt(x))
}

console.log(stringsToNumbers(["1","5"]))
console.log(stringsToNumbers())
console.log(stringsToNumbers([]))
console.log(stringsToNumbers(["a", "1"]))