#!/usr/bin/node
/**
 * A script that prints the addition of two integers
 */
let fNum = parseInt(process.argv[2]);
let sNum = parseInt(process.argv[3]);

function add(a, b){ return (a + b); }
console.log(add(fNum, sNum));
