#!/usr/bin/node
const index = process.argv;
if (isNaN(index[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + index[2]);
}
