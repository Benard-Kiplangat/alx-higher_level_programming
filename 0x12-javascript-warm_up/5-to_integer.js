#!/usr/bin/node
/*
 * A script that converts a string to int and prints it
 */
let myNum = parseInt(process.argv[2]);
if (isNaN(myNum))
	console.log("Not a number");
else
	console.log("My number: " + myNum);
