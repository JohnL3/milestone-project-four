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
let oneChecked= false;

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
    $('.author-sel').focus();
  } else {
    $('.author-input').css('display','none');
  }
});

$('.category').click(function(){
  if($('.category-input').css('display') === 'none') {
    $('.category-input').css('display','block');
    $('.author-input').css('display','none');
    $('.allergen-con').css('display','none');
    $('.category-sel').focus();
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

$('.clear-btn').click(function(){
    
     $('input:checkbox').prop('checked',false);
     $('input:radio').prop('checked',false);
     $('input:text').val('');
     addNames(categorys,'B');
     addNames(authors,'C');
     $(this).css('background','buttonface');
     $('.sub-btn').prop("disabled", true);
     oneChecked = false;
});
  
$('input:radio').click(function(){
    if($(this).prop('checked',true)){
        $('.clear-btn').css('background','lightblue');
        $('.sub-btn').prop("disabled", false);
        oneChecked = true;
    }
});
$('.filter-select-B').on('click', 'input:radio',function(){
   if($(this).prop('checked',true)){
        $('.clear-btn').css('background','lightblue');
        $('.sub-btn').prop("disabled", false);
        oneChecked = true;
    }
});

$('.filter-select-C').on('click', 'input:radio',function(){
   if($(this).prop('checked',true)){
        $('.clear-btn').css('background','lightblue');
        $('.sub-btn').prop("disabled", false);
        oneChecked = true;
    }
});



$('input:checkbox').click(function(){
    
    let ckboxIsCk = $('input[name="allergen"]:checked').length > 0
    if(ckboxIsCk === true){
        $('.clear-btn').css('background','lightblue');
        $('.sub-btn').prop("disabled", false);
        addFilteringItems();
    } else {
       if(oneChecked === false) {
           $('.clear-btn').css('background','buttonface');
           $('.sub-btn').prop("disabled", true);
           addFilteringItems();
       }
    }
});

// get a list of all category names
function getCategorys () {
    let categorys = [];
    let categorysTx = $('.category-tx');
    $( '.category-tx' ).each(function( ) {
      categorys.push($(this).text());
    });
    return categorys;
}

// get a list of all author names
function getAuthors () {
    let authors = [];
    let authorsTx = $('.author-tx');
    $( '.author-tx' ).each(function( ) {
      authors.push($(this).text());
    });
    return authors;
}
// set authors and categorys to  variables
let authors = getAuthors();
let categorys = getCategorys();

// for when typing in filter to filter categorys by letter
$( "input[name='category']" ).keyup(function(event) {
  
  let letter, list, word, ind;
  [letter, word, list, ind] = commonCode(event,this);
  console.log(ind);
  categorys.filter(function(x){
    if( letter === x.charAt(ind).toLocaleLowerCase() &&     x.toLocaleLowerCase().includes(word) && word !=''){
      list.push(x);
    } 
});
addNames(list,'B');
if(ind === -1) addNames(categorys,'B');
});

// for when typing in filter to filter authors by letter
$( "input[name='author']" ).keyup(function(event) {
  
  let letter, list, word, ind;
  [letter, word, list, ind] = commonCode(event,this);
  console.log(ind);
  authors.filter(function(x){
    if( letter === x.charAt(ind).toLocaleLowerCase() &&     x.toLocaleLowerCase().includes(word) && word !=''){
      list.push(x);
    } 
});
addNames(list,'C');
if(ind === -1) addNames(authors,'C');
});


let commonCode = function(e, t) {
  let letter = e.which;
  let word = $(t).val().toLocaleLowerCase();

  letter = String.fromCharCode(letter);
  letter = letter.toLowerCase();
  let list = [];
  let ind = word.length - 1;
  return [letter, word, list, ind];
};

let addNames = function(arr,ext) {
  let type = '';
  if(ext === 'B')  type = 'category';
  if(ext === 'C')  type = 'author';
  if(ext === 'A')  type = 'allergen';

  $('.inner-filter-'+ext).empty();

  for(let x=0; x< arr.length; x++) {
    let res = createInner(arr[x],type);
    $('.inner-filter-'+ext).append(res);
  }
};
//create html that shows filterd lists
let createInner = function(name, type) {
  let inner = `<div class='inner-divs'>
              <input type="radio" name='`+ type+`' value='' class=''><label>`+ name +`</label>
            </div>`;
            
    inner =`<div class='filter-inner'><input type='radio' name='category'><span class='category-tx'>`+name+`</span></div>`;
    return inner;
};

////
function addFilteringItems(){
  let allergens = [];
  $('.inner-filtering-by').empty();
  $('input[type=checkbox]').each(function () {
        if ($(this).is(":checked")){
          allergens.push($(this).attr('class'));
        } 
  });
  console.log(allergens);
  for (let itm in allergens) {
    let sp = '<span>'+allergens[itm]+'</span>';
    $('.inner-filtering-by').append(sp);
  }
  
}