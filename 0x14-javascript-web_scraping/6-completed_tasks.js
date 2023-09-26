#!/usr/bin/node

const request = require('request');

const args = process.argv;
const url = args[2];

request(url, (err, resp, body) => {
  if (err) return console.log(err);
  if (resp.statusCode !== 200) return console.log('Request Failed');

  const bodyJson = JSON.parse(body);

  const usersTodosCount = countUsersTodos(bodyJson);

  console.log(usersTodosCount);
});

function countUsersTodos (todos) {
  const countTable = todos.reduce((table, todo) => {
    table[todo.userId] = (table[todo.userId] ?? 0) + 1;
    return table;
  }, {});

  return countTable;
}
