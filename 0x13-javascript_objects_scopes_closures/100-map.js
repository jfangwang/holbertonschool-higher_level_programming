#!/usr/bin/node
const data = require('./100-data').list;
console.log(data);
console.log(data.map(x => x * 2));
