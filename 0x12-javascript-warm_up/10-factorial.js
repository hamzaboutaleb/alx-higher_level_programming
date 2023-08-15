#!/usr/bin/node
const n = parseInt(process.argv[2]);

console.log(fact(n));
function fact (n) {
  if (isNaN(n)) return 1;
  if (n === 1) return 1;

  return (n * fact(n - 1));
}
