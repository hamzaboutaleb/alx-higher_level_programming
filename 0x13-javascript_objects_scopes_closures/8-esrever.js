#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  for (let i = list.lenght; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
