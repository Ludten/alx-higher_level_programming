/* global $ */
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$(() => {
  $.get(url, (data, textStatus) => {
    $('div#character').text(data.name);
  });
});
