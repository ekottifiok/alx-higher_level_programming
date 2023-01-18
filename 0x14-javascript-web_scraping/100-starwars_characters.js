#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (error, _, body) {
  if (error) { console.log(error); } else {
    console.log(JSON.parse(body).characters.reduce((accumulator, element) => {
        if (accumulator) {
            accumulator += request('element', function (error, _, body) {
                if (error) { console.log(error); } else {body.name}
            }) + "\n"
        } else {
            accumulator = request('element', function (error, _, body) {
                if (error) { console.log(error); } else {body.name}
            })
        }
        return accumulator;
    }, null));
  }
});
