#!/usr/bin/node
/*
 * A script that converts a prints a square based on its argument
 */
const myNum = parseInt(process.argv[2]);
if (isNaN(myNum)) { console.log('Missing size'); } else {
  let i = myNum;
  let j = myNum;
  let square = '';
  while (i > 0) {
    while (j > 0) { square = square + ('X'); j--; }
    console.log(square);
    i--;
  }
}
