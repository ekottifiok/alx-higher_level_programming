#!/usr/bin/node
function add (a, b) {
  if (a && b) {
    return a + b;
  }
  return NaN;
}

console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
