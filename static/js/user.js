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
    $('form.user-page').css('display', 'block');
});

$('.inner-menu-a').click(function(){
    $('.grids').css('display', 'grid');
    $('form.user-page').css('display', 'none');
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

// function combining a ingredient and a quantity into an arry to keep them in pairs
function pair_ing_quan(ing_quan){
  let ing_and_quan = [];
  let inner = [];
  let count = 0;
  let r_len =  $('.ing :input[type=text]').length;
  let b_count = 0;
  
  ing_quan.each(function(){
  
    count++;
    b_count++;
    if(count === 3 ) {
        ing_and_quan.push([...inner]);
        inner=[];
        count=1;
      }
    inner.push($(this).val());
       
    if (b_count === r_len && inner.length != 0) ing_and_quan.push(inner);
    
  });
  
  return ing_and_quan;
}

// check fields are filled in or else add error class
function isNotBlank(items) {
    let result = true;
    items.each(function(){
        if($(this).val() === '') {
            result = false;
            $(this).addClass('error');
        }
    });
    return result;
}

function check_validation() {
  let ingAndQuan = isNotBlank($('.ing :input[type=text]'));
  let instructions = isNotBlank($('.step'));
  let author =  $('.author-inp').val();
  let recipeName = $('.recipe-inp').val();
  let category =  $( ".category-option option:selected" ).text();
  let prep = $('.prep-inp').val();
  let cook = $('.cook-inp').val();
  let serves = $('.serves-inp').val();
  
  
  
  if(!author || !recipeName  || !category  || !prep  || !cook  || !serves || ingAndQuan === false || instructions === false) {
    if(author === '') $('.author-inp').addClass('error');
    if(recipeName === '') $('.recipe-inp').addClass('error');
    if($( ".category-option option:selected" ).text() === '') $( ".category-option" ).addClass('error');
    if(prep === '') $('.prep-inp').addClass('error');
    if(cook === '') $('.cook-inp').addClass('error');
    if(serves === '') $('.serves-inp').addClass('error');
    $('html, body').animate({scrollTop: $("form").offset().top}, 500);
    
    setTimeout(function(){
       //$('.author-inp').removeClass('error');
       //$('.recipe-inp').removeClass('error');
       $( ".category-option" ).removeClass('error');
       $('input[type="text"]').removeClass('error');
       $('.step').removeClass('error');
    },2500);
    return false;
  } else {
    return true;
  }
}

// post details of new recipe to server
$('.sub-btn').click(function(event){
  event.preventDefault();
  // check all fields are filled in
  let validated = check_validation();
    
  if (validated) {
      
      // add pairs of ingredient and a quantity to  arrys
      let ing_and_quan = pair_ing_quan($('.ing :input[type=text]'));
            console.log(ing_and_quan);
        
      // add instructions to an array
      let instructions = [];
      $('.step').each(function() {
        instructions.push($(this).val());
      });
         
      // add allergens to an array
      let allergens=[];
      $('input[type=checkbox]').each(function () {
          if ($(this).is(":checked")){
            allergens.push('T');
          } else {
            allergens.push('F');
          }
      });
         
      // create data being pushed to server
      let data = {};
      data.author_name = $('.author-inp').val();
      data.recipe_name = $('.recipe-inp').val();
      data.category = $( ".category-option option:selected" ).text();
      data.allergens = allergens;
      data.instructions = instructions;
      data.ing_and_quan = ing_and_quan;
      data.prep = $('.prep-inp').val();
      data.cook = $('.cook-inp').val();
      data.serves = $('.serves-inp').val();
          
      console.log(data);
      //let url = 'http://our-cookbook-johnl3.c9users.io:8080/newrecipe';
      let url = 'https://our-cookbook-jl.herokuapp.com/newrecipe'
      $.ajax({
        type : 'POST',
        url : url,
        contentType: 'application/json;charset=UTF-8',
        dataType: 'json',
        data : JSON.stringify(data),
        success: function(data){
           console.log(data);
        }
      });
      
   }
});
