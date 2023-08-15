#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let num0ccurences = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) num0ccurences++;
  }
  return (num0ccurences);
};
