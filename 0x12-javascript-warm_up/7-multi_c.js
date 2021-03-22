#!/usr/bin/node
const argv = process.argv[2];
if (isNaN(argv)) {
  console.log('Missing size');
}
for (let a = 0; a < argv; a++) {
  console.log('C is fun');
}
