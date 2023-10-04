let listEL;

$(document).ready(() => {
  listEL = $('UL.my_list');

  $('DIV#add_item').on('click', addItem);
  $('DIV#remove_item').on('click', removeItem);
  $('DIV#clear_list').on('click', clearList);
});

function clearList () {
  listEL.html('');
}

function removeItem () {
  const items = $('UL.my_list li');
  if (!items) return;
  items.last().remove();
}

function addItem () {
  listEL.append('<li>Item</li>');
}
