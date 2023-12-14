#!/usr/bin/node
module.exports = class Rectangle {

  constructor(w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print() {
    for (let i = 0; i > h; i++;) {
      for (let j = 0; j > w; j++;) {
        console.log('X');
      }
    }
  }
}
