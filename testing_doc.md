# All about testing will be covered here.  

This project has manual testing only.  

I will talk about how I tested each page in the site.

## General Navigation Links 

Rather than repeat for each page I will cover navigation links here in one section, I visited every page as an user not logged in and visited every link
to make sure I was sent to the right page. I then logged in and repeated this process to make sure I was sent to the right page.

Links for pages are as follows  

- Home page will display recipe and either signup/login  or logout depending if user is logged in or not
- If logged in home page will show users name, recipe and logout

recipe page  
- links shown are home signup/login
- if logged in links are users name, home and logout

users page
- links show are home recipes logout

I clicked all these to make sure I was sent to the right page.  

### General layout for web pages

Rather than repeat I will cover general layout of web pages here

On mobile screens pages will have a header and underneath a navgation bar with a burger which you click to see navigation.  
On Tablets and desktops width 768 the navigation is in the header and navgation bar is not visible.  

I visited all pages in mobile sizes and made sure the navigation bar was visible and I clicked on the burger to make sure it opens and closes.  
I visited all pages for sizes 768 and up to make sure navigation bar was no longer visible and navigation was in the header.  

On recipe page there is also a filter bar, I visited this page to make sure it appears on both mobile sizes and larger.


If a user has logged in  

- I would expect to see a link to the users page : True
- I would expect to see logout : True


### Signup/Login page

There is a tabbed section with tab labelled signup and another labelled login.  
A form with a input for a username and an input for a password, and a button labelled signup.  

- If i click on the tab labelled login I would expect the tab to change color and button text to change to login : True
- If i click on the tab labelled signup I would expect the tab to change color and button text to change to signup : True

If I try to login in or signup without filling in both fields a message is displayed informing me I need to fill in the empty field : True  
If I signup successfully I am redirected to my user page : True  
If I login successfully I am redirected to my user page : True  


## Recipe Page

The recipe page contains a filter bar which is present in both mobile and larger screen views.  
The recipe page also contains cards of all the recipes created.

The recipe cards all contain a link to a view recipe page, where you can see the full recipe for that particular card.  
I tested this by clicking on the section that says view recipe, to make sure it brought me to a page showing me the full recipe.  

The recipe cards contain the following information  

- Recipe name
- Author name
- Category
- Allergens .. if the recipe contains allergens
- A like icon displaying the number of likes
- A collect icon displaying the number of times its being collected
- A view recipe link

The filter section.  

- Clicking on the filter should allow a dropdown to appear : True
- Clicking again should hide the dropdown : True
- The dropdown shows a top section of a submit button a clear button and a show all recipes button : True
- The bottom section shows a allergens button a category button and a authors button : True
- Submit button should initially be disabled and have a navajowhite background with a red border : True
- If an allergen or a category or an author is selected the submit button should no longer be disabled : True
- And the clear button should show a lightblue background and submit button should loose the background color and border color : True
- Clicking on the author button category button or allergen button should open there dropdown and close the other dropdowns: True
- Clicking on a author button category button or allergen button again should close dropdown for that specific button : True
- In the category or author you should only be able to select one name via the radio buttons : True
- If the clear button is pressed all radio button are set to off : True
- You should be able to select more than one item in the allergens dropdown : True
- Clicking the clear button clears all selected allergens : True

Filtering  

- You can filter by author : True
- You can filter by category : True
- You can filter by allergen : True
- You can filter by combination of any two ... author category allergen : True
- you can filter by using all three : True

- I clicked on author and selected Jack black and got back only recipes by Jack Black 
- I clicked on category and selected dessert and got back only recipes by category dessert.  
- I clicked on allergens and selected Egg and got back only recipes NOT containing Egg.  
- I clicked on allergens and selected Egg and Milk ang got back only recipes NOT containing Egg and Milk  
- I clicked on author Jack Black category dessert and got back only recipes that were dessert and Jack Black as author
- I clicked on category dessert and allergen Egg and got back recipes that were dessets and did not contain egg
- I clicked on author Jack Black category Dessert and allergen Milk and got back recipes by Jack Black that were dessert and did NOT contain milk

On desktop screens when author button or category button are clicked, as well as a dropdown list of categorys and authors there is an input 
that you can type into to filter the list by to make it easier if the list are long.  
I checked to make sure this is not visible on screen sizes samller than 1150px.  

I tested this by typing in the author section and watched it filter the names by letters pressed.  
I then tried it in the category seciton and filtered that list by typing in letters.  
I also tested to make sure when screen is resized and if list is filtered that it resets to full list.  


## User Page

On user page you have a tabbed section containing three tabs ... your recipes, collected, create recipe.  
The .. your recipe section is visible and if user has created recipes they will be shown beneath the tabs.  
If you click on collected you will be shown any recipes you have collected or statement saying you havent collected any recipes yet and if either of the other sections
had been visible at the time they would now be hidden.  
If you click on create recipe tab other sections would be hidden and a form for creating a recipe would appear.  

In the your recipe section are the reciipe cards which are the same as described above except for these have an edit button which when you click
opens a edit form with all recipe details for you to edit.  

Editing a recipe.  

- If no fields are changed and submit button is clicked nothing happens : True
- If a fild is cleared and you dont fill it with new information and submit button is clicked a error class is added to the field and form wont submit. : True
- Image field may be left empty, if it is the image you were using will remain the same. : True
- You can add a new url to change your recipe image, but if image is not of specified size you get a warning and will not be able to submit : True
- Allergen fields may be left empty if edit form shows them empty
- More Ingredients can be added or changed but cannot be removed : True
- Instructions can be added to or changed but not removed : True
- Fetch url button will show a preview of the image when clicked if you supply an url to the image : True
- The clear button will clear the url from the input and the image from the preview and the size from the text : True
- If you make a change to the recipe and click submit and all goes ok a message shows to say everything was updated and then page is refreshed and you 
- can observe the changes : True





 




