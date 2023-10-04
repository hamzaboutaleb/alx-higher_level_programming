const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';
const listEl = $('UL#list_movies');

$.ajax({
  url: URL,
  method: 'GET',
  dataType: 'json',
  success: ({ results }) => {
    results.forEach(movie => {
      listEl.append(`<li>${movie.title}</li>`);
    });
  }
});
