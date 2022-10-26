/* global $ */
const url = 'https://stefanbohacek.com/hellosalut/?lang=';
$(document).ready(() => {
  $('input#btn_translate').on('click', () => {
    const input = $('input#language_code').val();
    $.get(url + input, (data, textStatus) => {
      console.log(data);
      $('div#hello').text(data.hello);
    });
  });
});
