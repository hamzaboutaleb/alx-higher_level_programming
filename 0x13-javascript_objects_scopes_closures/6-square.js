#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.size; i++) {
      c += 'X';
    }
    for (let j = 0; j < this.size; j++) {
      console.log(c);
    }
  }
}

module.exports = Square;
