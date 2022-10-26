/* global $ */
const url = 'https://stefanbohacek.com/hellosalut/?lang=';
$(document).ready(() => {
  $('input#btn_translate').click(() => {
    const input = $('input#language_code').val();
    $.get(url + input, (data, textStatus) => {
      console.log(data);
      $('div#hello').text(data.hello);
    });
  });
  $('input#language_code').keypress((e) => {
    if (e.which === 13) { $('input#btn_translate').click(); }
  });
});
