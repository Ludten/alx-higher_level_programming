/* global $ */
$('div#toggle_header').on('click', () => {
  $('header').toggleClass('green')
    .toggleClass('red');
});
