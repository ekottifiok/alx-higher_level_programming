#!/usr/bin/node

const SquareRequired = require('./5-square');

// Write an empty class Rectangle that defines a rectangle.

module.exports = class Square extends SquareRequired {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      super.print(c);
    } else {
      for (let index = 0; index < this.height; index++) {
        for (let index2 = 0; index2 < this.width; index2++) {
          process.stdout.write(c);
        }
        console.log();
      }
    }
  }

  double () {
    super.double();
  }
};
