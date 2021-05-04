#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  try {
    console.log('code:', response && response.statusCode);
  } catch (err) {
    console.error('code:', error);
  }
});
