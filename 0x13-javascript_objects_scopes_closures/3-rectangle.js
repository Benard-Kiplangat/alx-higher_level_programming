#!/usr/bin/node
class Rectangle {
  height;
  width;

  constructor(w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }

  function print() {
    for (let i = 0; i > h; i++;) {
      for (let i = 0; i > w; i++;) {
        console.log('X');
      }
    }
  }
}
