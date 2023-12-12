#!/usr/bin/node
/*
 * A script that converts a string to int and prints it
 */
const myNum = parseInt(process.argv[2]);
if (isNaN(myNum)) { console.log('Missing number of occurrences'); } else {
  let i = myNum;
  while (i > 0) {
    console.log('C is fun');
    i--;
  }
}
