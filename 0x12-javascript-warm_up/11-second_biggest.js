#!/usr/bin/node

const len = process.argv.length;
if (len < 4) {
  console.log(0);
} else {
  let largest = parseInt(process.argv[2]);
  let secondLargest = parseInt(process.argv[3]);

  if (len === 4) {
    if (largest > secondLargest) {
      console.log(secondLargest);
    } else {
      console.log(largest);
    }
  } else {
    for (let index = 2; index < len; index++) {
      const x = parseInt(process.argv[index]);
      if (x > largest) {
        secondLargest = largest;
        largest = x;
      } else if (x > secondLargest) {
        secondLargest = x;
      }
    }
    console.log(secondLargest);
  }
}
