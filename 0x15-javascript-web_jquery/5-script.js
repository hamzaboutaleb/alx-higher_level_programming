const ulEl = $('UL.my_list');

$('DIV#add_item').on('click', () => {
  ulEl.append('<li>Item</li>');
});
