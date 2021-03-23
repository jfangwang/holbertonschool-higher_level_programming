#!/usr/bin/node
const data = require('./100-data').list;
console.log(data);
console.log(data.map((currentValue, index) => currentValue * index));
