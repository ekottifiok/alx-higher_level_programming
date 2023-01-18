#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, _, body) {
  if (error) { console.error(error); } else {
    console.log(JSON.parse(body).reduce((accumulator, element) => {
      if (element.completed) {
        if (accumulator[element.userId]) {
          accumulator[element.userId] += 1;
        } else {
          accumulator[element.userId] = 1;
        }
      }
      return accumulator;
    }, {})
    );
  }
});
