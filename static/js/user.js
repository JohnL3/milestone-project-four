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

// show and hide users recipes / collected/ create recipe
$('.inner-menu-c').click(function(){
    $('.grids').css('display', 'none');
    $(this).addClass('active-c');
    $('.all-collected').css('display', 'none');
    $('form.user-page').css('display', 'block');
    $('.inner-menu-a').removeClass('active-a');
    $('.inner-menu-b').removeClass('active-b');
    $('.inner-menu-c').removeClass('active-a');
    
});

$('.inner-menu-a').click(function(){
    $('.grids').css('display', 'grid');
    $('.all-collected').css('display', 'none');
    $('form.user-page').css('display', 'none');
    $('.user-inner-menu ul li').css('display', 'inline');
    $('.inner-menu-d').css('display', 'none');
    $('.edit-page').css('display', 'none');
    $('.inner-menu-a').addClass('active-a');
    $('.inner-menu-c').removeClass('active-c');
    $('.inner-menu-b').removeClass('active-b');
});

$('.inner-menu-b').click(function(){
    let allCollected = $('.all-collected');
    console.log(allCollected[0].childNodes.length);
    console.log(allCollected[0].childNodes);
    //$('.all-collected').empty();
    getCollectedRecipes();
    $('.inner-menu-c').removeClass('active-c');
    $('.inner-menu-b').addClass('active-b');
    $('.inner-menu-a').removeClass('active-a');
    $('.grids').css('display', 'none');
    $('.all-collected').css('display', 'grid');
    $('form.user-page').css('display', 'none');
});

$('.edit-recipe').click(function(){
    $('.user-inner-menu ul li').css('display', 'none');
    $('.inner-menu-a').css('display', 'inline');
    $('.inner-menu-d').css('display', 'inline');
    $('.inner-menu-a').removeClass('active-a');
    $('.inner-menu-d').addClass('active-c');
    $('.grids').css('display', 'none');
    $('.edit-page').css('display', 'block');

    let recipe_id = $(this).attr('id');
     let url = '/edit_recipe/'+ recipe_id;
     $.ajax({
        type : 'GET',
        url : url,
        success: function(data){
           console.log(data);
           
        }
      });
    
    console.log(recipe_id);
});

function getCollectedRecipes() {
    
    let url = '/collect';
      $.ajax({
        type : 'GET',
        url : url,
        success: function(data){
           console.log(data);
           if (data.length > 0) recipeTemplate(data);
           
           let allCollected = $('.all-collected');
           console.log(allCollected[0].childNodes.length);
           
        }
      });
}


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
            
        
      // add instructions to an array
      let instructions = [];
      $('.step').each(function() {
        instructions.push($(this).val());
      });
      instructions = instructions.join('_');
         
    
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
      data.category_name = $( ".category-option option:selected" ).text();
      data.allergens = allergens;
      data.instructions = instructions;
      data.ing_and_quan = ing_and_quan;
      data.prep = $('.prep-inp').val();
      data.cook = $('.cook-inp').val();
      data.serves = $('.serves-inp').val();
      data.username = $('.page-title').text();
      data.url ='/static/assets/images/dessert.jpg';
          
      console.log(data);
      let url = '/newrecipe';
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




function recipeTemplate(data) {
    $('.all-collected').empty();
    let allergen_spans = '';
    
    for(let items in data) {
        
        if(data[items].Egg === 'T'){
                allergen_spans += '<span class="allergen">Egg</span>';
            }
            if(data[items].Nuts === 'T'){
                allergen_spans += '<span class="allergen">Nut</span>';
                 
            }
            if(data[items].Moll === 'T'){
                allergen_spans += '<span class="allergen">Molluscs</span>';
            }
            if(data[items].Pnuts === 'T'){
                allergen_spans += '<span class="allergen">Peanuts</span>';
            }
            if(data[items].SBeans === 'T'){
                allergen_spans += '<span class="allergen">Soyabeans</span>';
            }
            if(data[items].Milk === 'T'){
                allergen_spans += '<span class="allergen">Milk</span>';
            }
            if(data[items].Celery === 'T'){
                allergen_spans += '<span class="allergen">Celery</span>';
            }
            if(data[items].Mustard === 'T'){
                allergen_spans += '<span class="allergen">Mustard</span>';
            }
            if(data[items].hasSSeeds === 'T'){
                allergen_spans += '<span class="allergen">Sesame Seeds</span>';
            }
            if(data[items].Fish === 'T'){
                allergen_spans += '<span class="allergen">Fish</span>';
            }
            if(data[items].Lupin === 'T'){
                allergen_spans += '<span class="allergen">Lupin</span>';
            }
            if(data[items].SDioxide === 'T'){
                allergen_spans += '<span class="allergen">Sulpher Dioxide</span>';
            }
            if(data[items].Cerals === 'T'){
                allergen_spans += '<span class="allergen">Cereals</span>';
            }
            if(data[items].Crust === 'T'){
                allergen_spans += '<span class="allergen">Crustaceans</span>';
            }
        
        let rHeader = `<div class="recipe-header">
                          <span>`+ data[items].recipe_name +`</span>
                        </div>`;
                        
        let imgCard = `<div class="my-img-card">
                          <img src='`+data[items].url+`'>
                        </div>`;
                        
        let rDetails = `<div class="recipe-details">
                            <div class="recipe-category">
                              <span>CATEGORY</span><span>`+data[items].category_name+`</span>
                            </div>
                            <div class="recipe-author">
                              <span>AUTHOR</span><span>`+data[items].author_name+`</span>
                            </div>
                          </div>`;
        let allergens = `<div class="recipe-allergens">
                            `+allergen_spans+`
                            </div>`;
                       
         
                            
        let section = `<div class='section-con'>
                        <div class="icons">
                          <div class="likes">
                            <i class="far fa-heart"></i>
                            <span>`+data[items].likes+`</span>
                          </div>
                          <div class="collect">
                            <i class="far fa-folder-open"></i>
                            <span>`+data[items].collected+`</span>
                          </div>
                        </div>
                        <div class='visit'>
                          <div>
                            <a class='view-span' href='/viewrecipe/`+data[items].recipe_name+`'>View Recipe</a>
                          </div>
                        </div>
                      </div>`;
                      
        let recipeBox = `<div class="recipe-box">
                            `+rDetails+`
                            <span>ALLERGENS</span>
                            `+allergens+`
                            `+section+`
                            </div>`; 
                            
        let outerDiv = `<div id="`+data[items].recipe_id+`" class="recipe">
                        `+ rHeader+`
                        `+imgCard+`
                        `+ recipeBox +`
                        </div>`;
                        
        $('.all-collected').append(outerDiv);
    }
}