#!/usr/bin/node

const request = require('request');

const args = process.argv;
const url = args[2];

request(url, (err, resp, body) => {
  if (err) return console.log(err);
  if (resp.statusCode !== 200) return console.log('Request failed');

  const { results } = JSON.parse(body);
  const countFilms = countWedgeFilms(results);

  console.log(countFilms);
});

function countWedgeFilms (movies) {
  const count = movies.reduce((acc, movie) => {
    if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) return acc + 1;
    return acc;
  }, 0);
  return count;
}
