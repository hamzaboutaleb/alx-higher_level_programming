#!/usr/bin/node
const argv = process.argv;
const length = argv.length - 2;
if (length === 0) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
