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


//used for the clicking on recipe and method page secion on viewrecipe page on mobile views
$('.li-first').click(function(){
    
   if($(this).css('background-color') === 'rgb(240, 128, 128)' && $(window).width() < 768) {
       $(this).css('background-color', '#f7bfbf');
       $(this).css('color', 'darkslategray');
       $('.li-second').css('background-color','#f08080');
       $('.li-second').css('color','white');
       $('.display-method').css('display', 'block');
        $('.display-ing').css('display', 'none');
   } else {
       $(this).css('background-color', '#f08080');
       $('.li-second').css('background-color','#f7bfbf');
       $(this).css('color', 'white');
       $('.li-second').css('color','darkslategray');
        $('.display-method').css('display', 'none');
        $('.display-ing').css('display', 'block');
   }
});

$('.li-second').click(function(){
   
    if($(this).css('background-color') === 'rgb(247, 191, 191)' && $(window).width() < 768) {
       $(this).css('background-color', '#f08080');
        $(this).css('color', 'white');
       $('.li-first').css('background-color','#f7bfbf');
       $('.li-first').css('color','darkslategray');
       $('.display-method').css('display', 'block');
       $('.display-ing').css('display', 'none');
   } else {
       $(this).css('background-color', '#f7bfbf');
         $('.li-first').css('background-color','#f08080');
         $(this).css('color', 'darkslategray');
         $('.li-first').css('color','white');
         $('.display-method').css('display', 'none');
         $('.display-ing').css('display', 'block');
   }
});