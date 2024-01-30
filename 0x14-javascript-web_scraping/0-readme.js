#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

fs.readFile(args[2], 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
