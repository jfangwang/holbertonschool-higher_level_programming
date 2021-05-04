#!/usr/bin/node
const number = process.argv[2];
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + number, function (error, response, body) {
  try {
    // console.log('code:', response && response.statusCode);
    const obj = JSON.parse(body);
    console.log(obj.title);
  } catch (err) {
    console.error('code:', error);
  }
});
