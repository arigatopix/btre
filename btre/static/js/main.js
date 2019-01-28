const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// jQuery
setTimeout(function() {
  $('#message').fadeOut('slow');
}, 3000);