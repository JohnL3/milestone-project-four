$('#burger').click(function(){
    if($('.nav-items').css('display') === 'none'){
        $('.nav-items').css('display','block');
    } else {
        $('.nav-items').css('display','none');
    }
});

// make it so menu items display on large screens if menu has been closed on small screen
$( window ).resize(function() {
  if($(window).width() > 767) {
       $('header').css('display', 'grid');
	   $('.nav-items').css('display','block');
  } else {
      $('.nav-items').css('display','none');
  }
});

// show and hide users recipes / create recipe
$('.inner-menu-c').click(function(){
    $('.grids').css('display', 'none');
    $('form').css('display', 'block');
});

$('.inner-menu-a').click(function(){
    $('.grids').css('display', 'block');
    $('form').css('display', 'none');
});

// Used to add extra lines of ingredients and quanties
$('.add-lines').click(function(){
  addOptions();
});

function addOptions() {
    $('.ing span').css('display','none');
    $('li').removeClass('special-li');
		var option = '<li class="other-li"><input type="text" ></li><li class="special-li"><input type="text"><span class="remove-ing">X</span></li>';
   $('.ing').append(option);
}

$(function(){
    $('.ing').on('click', 'span.remove-ing', function(){
       var rem = $(this).closest('li');
    $(rem).remove();
    $('.ing li:last').remove();
       });
});  



