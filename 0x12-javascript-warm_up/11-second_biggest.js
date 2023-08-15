#!/usr/bin/node

function second (array) {
  if (array.length <= 3) {
    return (0);
  }

  let max = 2;
  let secondMax = 3;

  for (let i = 3; i < array.length; i++) {
    const el = array[i];
    const elMax = array[max];

    if (el > elMax) max = i;
  }
  for (let i = 3; i < array.length; i++) {
    const el = array[i];
    const elMax = array[secondMax];
    if (el > elMax && max !== secondMax) secondMax = i;
  }
  return (array[secondMax]);
}

console.log(second(process.argv));
