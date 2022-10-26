/* global $ */
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$(() => {
  $.get(url, (data, textStatus) => {
    const titles = data.results;
    for (let i = 0; i < titles.length; i++) {
      $('ul#list_movies').append('<li>' + titles[i].title + '</li>');
    }
  });
});
