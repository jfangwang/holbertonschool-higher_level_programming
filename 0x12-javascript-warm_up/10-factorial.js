#!/usr/bin/node
function factorial(a) {
  if (a === 0 || isNaN(a)){
    return 1;
  }
  return a * factorial(a - 1);
}
let argv = process.argv;
console.log(factorial(argv[2]));
