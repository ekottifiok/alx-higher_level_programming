#!/usr/bin/node

function factorial (x) {
  if (x < 0) {
    return -1;
  }
  if (x === 1 || x === 0) {
    return 1;
  }
  return (x * factorial(x - 1));
}

const input = process.argv[2];
console.log(typeof input === 'undefined' ? 1 : factorial(parseInt(input)));
