#!/usr/bin/node
const dict = require('./101-data').dict;
const outputDict = {};
for (const key in dict) {
  // potential key will be a key's value
  const potentialKey = dict[key];
  // Push a new value if potential key exists
  if (outputDict[potentialKey] !== undefined) {
    outputDict[potentialKey].push(key);
  } else {
    // Create a new potentialKey
    outputDict[potentialKey] = [key];
  }
}
console.log(outputDict);
