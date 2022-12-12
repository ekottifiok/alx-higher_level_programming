#!/usr/bin/node

const smallArray = require('./100-data').list;

console.log(smallArray);
console.log(smallArray.map((value, index) => value * index));
