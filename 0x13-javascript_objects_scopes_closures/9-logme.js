#!/usr/bin/node

// prints the number of arguments already printed and the new argument value.
exports.logMe = function foo (item) {
  if (typeof foo.counter === 'undefined') {
    foo.counter = 0;
  }
  console.log(`${foo.counter}: ${item}`);
  foo.counter++;
};
