/* global $ */
const url = 'https://stefanbohacek.com/hellosalut/?lang=fr';
$(document).ready(() => {
  $.get(url, (data, textStatus) => {
    $('div#hello').text(data.hello);
  });
});
