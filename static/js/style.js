$(document).ready(function() {
  var nav = $('.hide-show');
  $(nav).hide();
  
  $('.toggle').click(function(e) {
      $(nav).slideToggle('slow');
      e.preventDefault();
  });
});

/*
$(document).on('submit', '#submit', function(e) {
  e.preventDefault();
  
  ajax({
    type: 'POST', 
    url: 'image/<int:pk>',
    data: {
       like: $('#like').val()
    },
    success: function(){
      
    }
  });
});
*/