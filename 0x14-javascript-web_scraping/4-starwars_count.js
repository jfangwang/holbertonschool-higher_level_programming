#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  try {
    // console.log('code:', response && response.statusCode);
    const obj = JSON.parse(body);
    let count = 0;
    // console.log(obj.results);
    // console.log(obj.results);
    for (let a = 0; a < obj.results.length; a++) {
      for (let b = 0; b < obj.results[a].characters.length; b++) {
        if (obj.results[a].characters[b] === 'https://swapi-api.hbtn.io/api/people/18/') {
          count += 1;
        }
      }
    }
    console.log(count);
  } catch (err) {
    console.error('code:', error);
  }
});
