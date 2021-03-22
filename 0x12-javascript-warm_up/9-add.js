#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(parseInt(a) + parseInt(b));
  }
}
const argv = process.argv;
add(argv[2], argv[3]);
