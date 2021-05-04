#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const obj = JSON.parse(body);
    let count = 0;
    for (let a = 0; a < obj.results.length; a++) {
      for (let b = 0; b < obj.results[a].characters.length; b++) {
        if (obj.results[a].characters[b].split('/')[5] === '18') {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
