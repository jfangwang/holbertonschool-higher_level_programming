#!/usr/bin/node
const argv = process.argv[2];
if (isNaN(argv)) {
  console.log('Missing size');
}
for (let a = 0; a < argv; a++) {
  for (let b = 0; b < argv; b++) {
    process.stdout.write('X');
  }
  console.log('');
}
