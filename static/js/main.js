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
      $('input:text').val('');
      addNames(categorys,'B');
      addNames(authors,'C');
      $('.clear-btn').css('background','buttonface');
      $('.sub-btn').prop("disabled", true);
      oneChecked = false;
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
 
  $('.inner-filter-'+ext).empty();

  for(let x=0; x< arr.length; x++) {
    let res = createInner(arr[x]);
    $('.inner-filter-'+ext).append(res);
  }
};
//create html that shows filterd lists
let createInner = function(name) {
    let inner =`<div class='filter-inner'><input type='radio' name='category'><span class='category-tx'>`+name+`</span></div>`;
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

$('.sub-btn').click(function(){
    let allergens = [];
    let data = {};
    
    let ckboxIsCk = $('input[name="allergen"]:checked').length > 0;
    let rdIsCkA = $('input[name="author"]:checked').length > 0;
    let rdIsCkC = $('input[name="category"]:checked').length > 0;
    
     //$('.filter-select-A').css('display', 'none');
     //$('.filter-select-B').css('display', 'none');
     //$('.filter-select-C').css('display', 'none');
     
     $('.allergen-con').css('display','none');
     $('.category-input').css('display','none');
     $('.author-input').css('display','none');
            
    if(ckboxIsCk === true || rdIsCkA === true || rdIsCkC === true) {
       
       $('.clear-btn').css('background','buttonface');
       
       if (ckboxIsCk === true) {
           $('input[type=checkbox]').each(function () {
                  if ($(this).is(":checked")){
                    allergens.push($(this).attr('class'));
                  } 
            });
           data.allergens = allergens;
       }
       
       if(rdIsCkC === true) {
          let cat = $('input[name="category"]:checked').val();
          data.category_name = cat;
       }
       
       if(rdIsCkA === true) {
          let aut = $('input[name="author"]:checked').val();
          data.author_name = aut;
         
       }
       $('input:checkbox').prop('checked',false);
       $('input:radio').prop('checked',false);
       $('.sub-btn').prop('disabled', true)
       
       console.log(data);
       let url = '/filter_recipes';
       
        $.ajax({
            type : 'POST',
            url : url,
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            data : JSON.stringify(data),
            success: function(d){
               createRecipesDivs(d);
            }
        }); 
    }
});

$('.all-recipe-btn').click(function(){
    
    let url = '/get_all';
      $.ajax({
        type : 'GET',
        url : url,
        success: function(data){
           console.log(data);
           createRecipesDivs(data);
        }
      });
    
});


function createRecipesDivs(data) {
    $('.grids').empty();
    let allergen_spans = '';
    
    for (let x=0; x<data.length;x++){
        
            if(data[x].Egg === 'T'){
                allergen_spans += '<span class="allergen">Egg</span>';
            }
            if(data[x].Nuts === 'T'){
                allergen_spans += '<span class="allergen">Nut</span>';
                 
            }
            if(data[x].Moll === 'T'){
                allergen_spans += '<span class="allergen">Molluscs</span>';
            }
            if(data[x].Pnuts === 'T'){
                allergen_spans += '<span class="allergen">Peanuts</span>';
            }
            if(data[x].SBeans === 'T'){
                allergen_spans += '<span class="allergen">Soyabeans</span>';
            }
            if(data[x].Milk === 'T'){
                allergen_spans += '<span class="allergen">Milk</span>';
            }
            if(data[x].Celery === 'T'){
                allergen_spans += '<span class="allergen">Celery</span>';
            }
            if(data[x].Mustard === 'T'){
                allergen_spans += '<span class="allergen">Mustard</span>';
            }
            if(data[x].SSeeds === 'T'){
                allergen_spans += '<span class="allergen">Sesame Seeds</span>';
            }
            if(data[x].Fish === 'T'){
                allergen_spans += '<span class="allergen">Fish</span>';
            }
            if(data[x].Lupin === 'T'){
                allergen_spans += '<span class="allergen">Lupin</span>';
            }
            if(data[x].SDioxide === 'T'){
                allergen_spans += '<span class="allergen">Sulpher Dioxide</span>';
            }
            if(data[x].Cerals === 'T'){
                allergen_spans += '<span class="allergen">Cereals</span>';
            }
            if(data[x].Crust === 'T'){
                allergen_spans += '<span class="allergen">Crustaceans</span>';
            }
            
            let recipeHeader =`<div class='recipe-header'><span>`+data[x].recipe_name+`</span></div>`;
            let imgCard = `<div class='my-img-card'><img src='`+data[x].url+`'></div>`;
            
            
            let recipeBox = `<div class='recipe-box'>
                                <div class='recipe-deatils'>
                                  <div class='recipe-category'>
                                    <span>CATEGORY</span>
                                    <span class='category-name'>`+data[x].category_name+`</span>
                                  </div>
                                  <div class='recipe-author'>
                                    <span>AUTHOR</span>
                                    <span class='author-name'>`+data[x].author_name+`</span>
                                  </div>
                                </div>
                                <span>ALLERGENS</span>
                                <div class='recipe-allergens'>
                                  `+allergen_spans+`
                                </div>
                                <div class='section-con'>
                                  <div class='icons'>
                                   <div class='likes'>
                                    <i class='far fa-heart'></i>
                                    <span>`+data[x].likes+`</span>
                                   </div>
                                    <div class='collect'>
                                      <i class='far fa-folder-open'></i>
                                      <span>`+data[x].collected+`</span>
                                    </div>
                                  </div>
                                  <div class='visit'>
                                    <div>
                                      <a class='view-span' href='/viewrecipe/`+data[x].recipe_name+`'>View Recipe</a>
                                    </div>
                                  </div>
                                </div>
                              </div>`;
                              
            let outerDiv = `<div id='`+data[x].recipe_id+`' class='recipe'>
                              `+recipeHeader+`
                               `+imgCard+`
                               `+recipeBox+`
                            </div>`;
            
            $('.grids').append(outerDiv);
            
            allergen_spans = '';
    }
}

