#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let x = '';
    for (let i = 0; i < this.w; i++) {
      x += 'X';
    }
    for (let i = 0; i < this.h; i++) {
      console.log(x);
    }
  }
};
