$(document).ready(function() {
  var nav = $('.hide-show');
  $(nav).hide();
  
  $('.toggle').click(function(e) {
      $(nav).slideToggle('slow');
      e.preventDefault();
  });
});