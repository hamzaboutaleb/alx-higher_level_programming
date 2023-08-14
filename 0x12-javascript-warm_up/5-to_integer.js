#!/usr/bin/node
const isNumber = (num) => !isNaN(parseInt(num));
if (!isNumber(process.argv[2])) {
  console.log('Not a number')
} else {
  console.log('My number: ' + process.argv[2]);
}
