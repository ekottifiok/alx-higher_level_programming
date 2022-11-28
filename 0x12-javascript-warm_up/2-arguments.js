#!/usr/bin/node
if (require('node:process').argv.length > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
