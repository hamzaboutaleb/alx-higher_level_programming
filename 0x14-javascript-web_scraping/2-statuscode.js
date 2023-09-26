#!/usr/bin/node

const request = require('request');

const args = process.argv;
const url = args[2];

request(url, (err, response) => {
  if (err) console.log(err);
  console.log(`code: ${response.statusCode}`);
});
