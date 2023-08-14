#!/usr/bin/node

function second (array) {
  if (array.length <= 3) {
    return (0);
  }

  let max = array[2];
  let secondMax = array[3];

  for (let i = 2; i < array.length; i++) {
    if (array[i] > max) {
      secondMax = max;
      max = array[i];
    } else if (array[i] > secondMax && array[i] < max) {
      secondMax = array[i];
    }
  }
  return (secondMax);
}

console.log(second(process.argv));
