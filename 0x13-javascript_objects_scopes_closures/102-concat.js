#!/usr/bin/node

const fs = require('fs');
let content = '';

content.concat(fs.readFileSync(process.argv[2]));
content.concat(fs.readFileSync(process.argv[3]));
fs.writeFileSync(process.argv[4], content);