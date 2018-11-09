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


 




