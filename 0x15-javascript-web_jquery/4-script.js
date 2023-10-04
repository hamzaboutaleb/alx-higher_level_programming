$('DIV#toggle_header').on('click', () => {
  const headerEl = $('header');

  if (headerEl.hasClass('red')) {
    headerEl.removeClass('red');
    headerEl.addClass('green');
  } else {
    headerEl.removeClass('green');
    headerEl.addClass('red');
  }
});
