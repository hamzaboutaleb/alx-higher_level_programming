let langInput, btnEL, helloEl;

$(document).ready(() => {
  langInput = $('INPUT#language_code');
  btnEL = $('INPUT#btn_translate');
  helloEl = $('DIV#hello');

  btnEL.on('click', handleRequest);
  langInput.on('keydown', handleInputKey);
});

function handleInputKey (e) {
  if (e.key !== 'Enter') return;
  handleRequest();
}

function handleRequest () {
  const langCode = langInput.val();
  if (!langCode) return;
  $.ajax({
    url: url(langCode),
    method: 'GET',
    dataType: 'json',
    success: ({ hello }) => {
      helloEl.text(hello);
      langInput.val('');
    }
  });
}

function url (lang) {
  return `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
}
