#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const args = process.argv;
const url = args[2];
const filePath = args[3];

request(url, (err, resp, body) => {
  if (err) return console.log(err);
  if (resp.statusCode !== 200) return console.log('Request failed');

  writeTo(filePath, body);

});

function writeTo (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', err => {
    if (err) return console.log(err);
  });
}
