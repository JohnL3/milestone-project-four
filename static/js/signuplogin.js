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

$('.login-tab').click(function(){
    $(this).css('background', 'lightcoral');
    $(this).css('color', 'white');
    $('.signup-tab').css('background', '#f7bfbf');
    $('.signup-tab').css('color', 'darkslategray');
    $('button').text('LOGIN');
    $('form').attr('action', 'http://our-cookbook-johnl3.c9users.io:8080/login');
});

$('.signup-tab').click(function(){
    $(this).css('background', 'lightcoral');
    $(this).css('color', 'white');
    $('.login-tab').css('background', '#f7bfbf');
    $('.login-tab').css('color', 'darkslategray');
    $('button').text('SIGN UP');
     //'https://our-cookbook-jl.herokuapp.com/signup'
     //'http://our-cookbook-johnl3.c9users.io:8080'
    $('form').attr('action', 'http://our-cookbook-johnl3.c9users.io:8080/signup');
});