$(document).ready(function() {
  
  //Mobile design slide down menu
  var nav = $('.hide-show');
  $(nav).hide();
  
  $('.toggle').click(function(e) {
      $(nav).slideToggle('slow');
      e.preventDefault();
  });
  
  
  //Ajax to like button without refresh
  $('.img-like').on('submit', function(e) {
    e.preventDefault();
    var id = $(this).attr('data-id')
    var likes = Number($(this).attr('data-likes'))
    var formElement = $(this)
    var token = $(this).children('input[name=csrfmiddlewaretoken]').val();
    var button = $(this).children('button')
    $.ajax({
      type: 'POST', 
      url: `/details/image/${id}`,
      data: {
        like: $('#like').val(),
        csrfmiddlewaretoken: token
      },
      success: function(){
        likes +=1
        formElement.attr('data-likes', likes)
        button.html(likes)
      }
    });
  });
});


