#!/usr/bin/node
const argv = process.argv;
let max = 0;
if (argv.length <= 3) {
  console.log(0);
} else {
  max = argv[2];
  for (let i = 3; i < argv.length; i++) {
    let num = parseInt(argv[i]);
    if (num > max) max = num;
  }
  console.log(max);
}