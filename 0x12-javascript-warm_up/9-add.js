#!/usr/bin/node
/**
 * A script that prints the addition of two integers
 */
const fNum = parseInt(process.argv[2]);
const sNum = parseInt(process.argv[3]);

function add (a, b) { return (a + b); }
console.log(add(fNum, sNum));
