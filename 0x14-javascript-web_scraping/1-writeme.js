#!/usr/bin/node
const file = process.argv[2];
const content = process.argv[3];
const fs = require('fs');
try {
  const data = fs.writeFileSync(file, content)
} catch (err) {
  console.error(err)
}