#!/usr/bin/node
const argv = process.argv;
let max = 0, max2 = 2;
if (argv.length <= 3) {
  console.log(0);
} else {
  max = 2;

  for (let i = 3; i < argv.length; i++) {
    let num = parseInt(argv[i]);
    if (num > argv[max]) max = i;
  }
  for (let i = 2; i < argv.length; i++) {
    let num = parseInt(argv[i]);
    if (num > argv[max2] && i != max) max2 = i;
  }
  console.log(argv[max2]);
}