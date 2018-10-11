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
    $('.grids').css('display', 'grid');
    $('form').css('display', 'none');
});

// Used to add extra lines of ingredients and quanties
$('.adding-lines').click(function(){
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

// for adding extra textarea for instructions in create recipe section

$('.add-textarea').click(function(){
    addTextarea();
});

function addTextarea() {
    var option = `<textarea rows="3" class='step' placeholder='Step 3 ' ></textarea>`;
    $('.instructions-con').append(option);
}

// function doing two jobs: 1st combining a ingredient and a quantity into an arry to keep them in pairs
// 2nd to add error if only an ingredient or quantity is added and set return array to [] so user can fill in missing one
function pair_ing_quan(ing_quan){
  let ing_and_quan = [];
  let inner = [];
  let count = 0;
  let r_len =  $('.ing :input[type=text]').length;
  let b_count = 0;
  let all_ok = true;
  
  ing_quan.each(function(){
    if(all_ok === true) {
        if($(this).val() != ''){ 
          count++;
          b_count++;
          if(count === 3 ) {
            ing_and_quan.push([...inner]);
            inner=[];
            count=1;
          }
          inner.push($(this).val());
       } else{
         //count++;
         //b_count++;
         all_ok = false;
         $(this).addClass('error');
       }
      if (b_count === r_len && inner.length != 0) ing_and_quan.push(inner);
      
    }
    
  });
  
  return (all_ok)? ing_and_quan: [];
}

function check_validation(r_q, ins) {
  
  let author =  $('.author-inp').val();
  let recipeName = $('.recipe-inp').val();
  let category =  $( ".category-option option:selected" ).text();
  let prep = $('.prep-inp').val();;
  let cook = $('.cook-inp').val();;
  
  if(author === '' || recipeName === '' || category === '' || prep === '' || cook === '' || r_q.length < 1) {
    if(author === '') $('.author-inp').addClass('error');
    if(recipeName === '') $('.recipe-inp').addClass('error');
    if($( ".category-option option:selected" ).text() === '') $( ".category-option" ).addClass('error');
    if(prep === '') $('.prep-inp').addClass('error');
    if(cook === '') $('.cook-inp').addClass('error');
    $('html, body').animate({scrollTop: $("form").offset().top}, 500);
    
    setTimeout(function(){
       //$('.author-inp').removeClass('error');
       //$('.recipe-inp').removeClass('error');
       $( ".category-option" ).removeClass('error');
       $('input[type="text"]').removeClass('error');
    },2500);
    return false;
  } else {
    return true;
  }
}

$('.sub-btn').click(function(event){
    event.preventDefault();
    let ing_and_quan = pair_ing_quan($('.ing :input[type=text]'));
    console.log(ing_and_quan);
    let instructions ='';
    let validated = check_validation(ing_and_quan, instructions);
});