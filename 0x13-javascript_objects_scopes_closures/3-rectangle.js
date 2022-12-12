#!/usr/bin/node
// Write an empty class Rectangle that defines a rectangle.

module.exports = class Rectangle {
  constructor (width, height) {
    if (typeof width === 'number' && typeof height === 'number' &&
            width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    for (let index = 0; index < this.height; index++) {
      for (let index2 = 0; index2 < this.width; index2++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
};
