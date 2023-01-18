#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, _, body) {
  if (error) { console.error(error); } else {
    console.log(JSON.parse(body).results.filter((item) => {
      return item.characters.filter((item) => {
        return item.includes('18');
      }).length;
    }).length
    );
  }
});
