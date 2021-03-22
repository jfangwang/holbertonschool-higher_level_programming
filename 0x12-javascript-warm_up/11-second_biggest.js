#!/usr/bin/node
const argv = process.argv;
let big = 0;
for (let a = 2; a < argv.length; a++) {
  if (parseInt(argv[a]) > big) {
    big = parseInt(argv[a]);
  }
}
console.log(big);
