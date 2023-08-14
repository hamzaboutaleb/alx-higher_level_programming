#!/usr/bin/node
const n = process.argv[2];

console.log(fact(n));
function fact(n) {
  if (isNaN(n)) return 1;
  if (n == 0) return 1;

  return n * fact(n-1);
}
