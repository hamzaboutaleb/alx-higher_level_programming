#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

for (const [key, value] of dict.entries()) {
  newDict[value] = newDict[value]?.push(key) || [];
}

console.log(newDict);
