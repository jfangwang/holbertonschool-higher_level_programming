#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const dict = {};
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const obj = JSON.parse(body);
    for (let a = 0; a < obj.length; a++) {
      if (obj[a].completed === true) {
        dict[obj[a].userId] = (dict[obj[a].userId] || 0) + 1;
      }
    }
    console.log(dict);
  }
});
