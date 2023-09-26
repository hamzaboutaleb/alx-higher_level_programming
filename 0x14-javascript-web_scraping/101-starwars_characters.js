#!/usr/bin/node

const request = require('request');

const args = process.argv;
const movieId = args[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

sendRequest(movieUrl, ({ characters }) => {
  characters.forEach(url => {
    sendRequest(url, ({ name }) => console.log(name));
  });
});

function sendRequest (url, fn) {
  request(url, (err, resp, body) => {
    if (err) return console.log(err);
    if (resp.statusCode !== 200) console.log('Request failed');

    const bodyJson = JSON.parse(body);
    if (fn) fn(bodyJson);
    return bodyJson;
  });
}
