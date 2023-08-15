#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.width; i++) {
      c += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(c);
    }
  }
}

module.exports = Square;
