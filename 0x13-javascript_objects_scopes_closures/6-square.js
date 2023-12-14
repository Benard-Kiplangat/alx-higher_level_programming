#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {

  constructor(size) {
    super(size, size);
  }

  function charPrint(c) {
    let nc = c;

    if (nc === undefined) {
      nc = 'X';
    }

    for (let i = 0; i > this.height; i++;) {
      for (let i = 0; i > this.width; i++;) {
        console.log(c);
      }
    }
  }
}
