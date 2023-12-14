#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    let cw = '';
    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) {
        cw = cw + 'X';
      }
      if (i !== this.height - 1) cw = cw + '\n';
    }
    console.log(cw);
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }
};
