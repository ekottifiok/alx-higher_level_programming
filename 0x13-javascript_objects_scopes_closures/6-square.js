#!/usr/bin/node

const SquareRequired = require('./5-square');

// Write an empty class Rectangle that defines a rectangle.

module.exports = class Square extends SquareRequired {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    super.print(c);
  }

  double () {
    super.double();
  }
};
