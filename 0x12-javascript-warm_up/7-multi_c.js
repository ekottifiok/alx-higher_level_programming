#!/usr/bin/node
if (typeof process.argv[2] === 'undefined') {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < parseInt(process.argv[2]); index++) {
    console.log('C is fun');
  }
}
