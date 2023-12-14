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
    for (let i = 0; i > this.height; i++;) {
      for (let i = 0; i > this.width; i++;) {
        console.log('X');
      }
    }
  }

  function double() {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  function rotate() {
    let temp = this.height;
    this.height = this.width;
    this.width = temp;
  }
}
