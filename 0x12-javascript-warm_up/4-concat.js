#!/usr/bin/node
const index = process.argv;
let first = 'undefined';
let second = 'undefined';
if (index[2] !== undefined) {
  first = index[2];
}
if (index[3] !== undefined) {
  second = index[3];
}
console.log(first + ' is ' + second);
