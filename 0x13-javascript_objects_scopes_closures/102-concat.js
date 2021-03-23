#!/usr/bin/node
// Module required to use file selector
const fs = require('fs');
const fileA = fs.readFileSync('fileA', 'utf-8');
const fileB = fs.readFileSync('fileB', 'utf-8');
for (let a in process.argv) {
    console.log(a);
}
//fs.writeFileSync('fileC', fileA + '\n' + fileB);
