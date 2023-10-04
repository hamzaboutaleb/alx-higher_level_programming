const URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$(document).ready(() => {
  $.ajax({
    url: URL,
    method: 'GET',
    dataType: 'json',
    success: ({ hello }) => {
      $('DIV#hello').text(hello);
    }
  });
});
