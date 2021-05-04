#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  console.error('code:', error); // Print the error if one occurred
  console.log('code:', response && response.statusCode); // Print the response status code if a response was received
});
