#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {

  constructor(size) {
    super(size, size);
  }

  charPrint(c = 'X') {
    let cw = ''
    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) {
        cw = cw + c;
      }
      if (i !== this.height - 1) cw = cw + '\n';
    }
    console.log(cw);
  }
}
