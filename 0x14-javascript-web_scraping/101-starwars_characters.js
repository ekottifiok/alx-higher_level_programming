#!/usr/bin/node

const request = require('request');

function handleRequest (array, iter) {
  if (array.length === iter) return;
  request(array[iter], function (error, _, body) {
    if (error) { console.log(error); } else {
      console.log(JSON.parse(body).name);
    }
    handleRequest(array, iter + 1);
  });
}

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (error, _, body) {
  if (error) { console.log(error); } else { handleRequest(JSON.parse(body).characters, 0); }
});
