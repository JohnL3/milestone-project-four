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

/************************* Recipe Page Filter *********************************************/

$('.filters-header').click(function(){
  if($('.filter-items-con').css('display') === 'none') {
  
    $('.filter-items-con').css('display','block');
    
    if($(window).width() < 768) {
        $('nav').css('display','none');
        $('header').css('display','none');
    }
  } else {
      if($(window).width() > 767){
        $('nav').css('display','inline-block');
        $('header').css('display','grid');
      } else {
        $('nav').css('display','block');
        $('header').css('display','block');
      }
    $('.filter-items').css('display','block');

    $('.filter-items-con').css('display','none');
    $('.type').css('display','none');
  }
});

$('.author').click(function(){
  if($('.author-input').css('display') === 'none') {
    $('.author-input').css('display','block');
    $('.category-input').css('display','none');
    $('.allergen-con').css('display','none');
  } else {
    $('.author-input').css('display','none');
  }
});

$('.category').click(function(){
  if($('.category-input').css('display') === 'none') {
    $('.category-input').css('display','block');
    $('.author-input').css('display','none');
    $('.allergen-con').css('display','none');
  } else {
    $('.category-input').css('display','none');
  }
});

$('.allergen').click(function(){
  if($('.allergen-con').css('display') === 'none') {
    $('.allergen-con').css('display','block');
    $('.category-input').css('display','none');
    $('.author-input').css('display','none');
  } else {
    $('.allergen-con').css('display','none');
  }
});

