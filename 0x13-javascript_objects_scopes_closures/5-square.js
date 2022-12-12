#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// Write an empty class Rectangle that defines a rectangle.

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
