#!/usr/bin/node
/**
 * A script that computes a factorial
 */
const myNum = parseInt(process.argv[2]);

function factorial (num) {
  if (isNaN(num)) { return (1); }
  if (num === 1) { return (1); }
  return (num * factorial(num - 1));
}
console.log(factorial(myNum));
