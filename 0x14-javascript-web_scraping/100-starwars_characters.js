#!/usr/bin/node
const MovieNum = process.argv[2];
const request = require('request');
let url = 'https://swapi-api.hbtn.io/api/people/';
const PeepList = ['https://swapi-api.hbtn.io/api/people/',
  'https://swapi-api.hbtn.io/api/people/?page=2',
  'https://swapi-api.hbtn.io/api/people/?page=3',
  'https://swapi-api.hbtn.io/api/people/?page=4',
  'https://swapi-api.hbtn.io/api/people/?page=5',
  'https://swapi-api.hbtn.io/api/people/?page=6',
  'https://swapi-api.hbtn.io/api/people/?page=7',
  'https://swapi-api.hbtn.io/api/people/?page=8',
  'https://swapi-api.hbtn.io/api/people/?page=9'
];
for (const a in PeepList) {
  url = PeepList[a];
  request(url, function (error, response, body) {
    if (error) {
      console.error(error);
    } else {
      const obj = JSON.parse(body);
      const res = JSON.parse(body).results;
      url = obj.next;
      for (let a = 0; a < res.length; a++) {
        for (const b in res[a].films) {
          if (res[a].films[b].split('/')[5] === MovieNum) {
            console.log(res[a].name);
          }
        }
      }
    }
  });
}
