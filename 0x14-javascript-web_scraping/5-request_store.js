#!/usr/bin/node
const url = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fs = require('fs');
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFileSync(file, body, error);
  }
});
