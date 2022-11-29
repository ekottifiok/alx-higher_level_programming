#!/usr/bin/node

let x, y = -9999999999999, z = -9999999999999;

process.argv.forEach((val, index) => {
    if (index >= 2) {
        x = parseInt(val);
        if (x > y) {
            z = y;
            y = x;
        }

    }
});
console.log(y);
console.log(z);
