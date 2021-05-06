#!/usr/bin/node
const url = process.argv[1];
const fs = require('fs');
try {
  const data = fs.readFileSync(url, 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
