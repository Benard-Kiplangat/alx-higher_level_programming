#!/usr/bin/node
/**
 * A script that prints the second biggest integer in the list of arguments
 */
const myNum = [];

for (let i = 2; process.argv[i]; i++) {
  myNum[i - 2] = parseInt(process.argv[i]);
}
console.log(myNum);
myNum.sort((a, b) => a - b);
console.log(myNum);
myNum.reverse();
console.log(myNum);
if (myNum[0] === undefined) { console.log(0); } else if (myNum.length === 1) { console.log(0); } else console.log(myNum[1]);
