#!/usr/bin/node
// Module required to use file selector
const fs = require('fs');
if (process.argv.length === 5) {
  const argv = process.argv;
  const fileA = fs.readFileSync(argv[2], 'utf-8');
  const fileB = fs.readFileSync(argv[3], 'utf-8');
  fs.writeFileSync(argv[4], fileA + '\n' + fileB);
} else {
  console.log('USAGE: ./102-concat.js File1 File2 DestFile');
}
