#!/usr/bin/node

const request = require('request');

const args = process.argv;
const movieId = args[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, response, body) => {
  if (err) return console.log(err);
  if (response.statusCode !== 200) return console.log('Request failed');

  const { title } = JSON.parse(body);
  console.log(title);
});
