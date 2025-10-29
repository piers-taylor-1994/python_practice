// function stringsToNumbers(arr) {
//     if (arr && arr.length) {
//         return arr.map(x => parseInt(x))
//     }
// }

// console.log(stringsToNumbers(["1","5"]))
// console.log(stringsToNumbers())
// console.log(stringsToNumbers([]))
// console.log(stringsToNumbers(["a", "1"]))

// let array = [1,2,3]

// for (let index = 0; index < array.length; index++) {
//     console.log(array[index]);
// }

// array.forEach(element => {
//     console.info(element)
// });

// if (0) console.log("Test!!")

// const student = {
//     firstName: "George"
// }

// const {firstName : displayName} = student;

function computerCheckDigit(identificationNumber) {
    let result = 0;
    let oddIndexSum = 0;

    for (let i = 0; i < identificationNumber.length; i++) {
        if (i % 2 == 0) {
            result += Number(identificationNumber[i]);
        }
        else {
            oddIndexSum += Number(identificationNumber[i]);
        }
    }

    result = result * 3
    result = result + oddIndexSum

    let resultString = result.toString()
    let resultStringLength = resultString.length
    let lastDigit = resultString[resultStringLength - 1]

    if (lastDigit == "0") {
        return 0
    }
    else {
        return 10 - Number(lastDigit)
    }
}

function Test(table, criteria) {
    return table.sort((a, b) => b[criteria] - a[criteria])
}

const people = [
  { age: 30 },
  { age: 25 },
  { age: 35 }
];


console.log(Test(people, "age"))