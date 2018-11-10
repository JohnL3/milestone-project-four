# Milestone Project 4
Project hosted at: [Our Cook Book](https://our-cookbook-jl.herokuapp.com/)  

A website for people who like to look at different recipes, and are looking for somewhere to store there collection of recipes.

## UX

This website is for everybody who enjoys finding different recipes to try out or want to share there recipes or just to store there recipes.  
As a user I should be able visti the site and have options to signup login or view recipes.  
This is a achieved on the landing page where you have links to a signup/login section and a link to the recipe page which shows all the recipes.  
As a user I should have my own page Where I can  
- Create recipes
- See Just recipes I created
- Collect recipes I am interested in
- Edit my recipes 

This is achieved when you signup, you are directed to your own page where you can create recipes, view your recipes, collect recipes and edit your own recipes.  

As a user I should be able to collect other peoples recipes.  
This is achieved on the view a recipe page where there is a icon you can click on and it will add it to the collect recipe section of your page.  

As a user I should be able to like recipes.  
This is achieved on the view recipe page where there is a icon you can click on and it will register your like.  

As a user I should be able to filter recipes.  
This is achieved on the recipe page and you can filter recipes by author, category, allergens or mixture of two categorys or of all three.  

## Features

- A signup/login page ... where you can choose a username to use and a password.  
- A user page where you can view recipes that you create, a section for recipes you collect, a section for creating a recipe and where you can edit your recipes.  
- Filters ... which can be found on the recipe page. Giving you the option to filter recipes so you can find what you are looking for easier.  

 
## Future Features

- Ability to not show certain recipes, I would like to implement this, and give users the ability to block content showing that they might not want to see.
- Ability to show count of all recipes, most collected. It would be nice to be able to show this kind of information.

## Technologies Used

1. cloud9
 + Recommended by course
 + ['Cloud9'](https://ide.c9.io/)
2. jQuery
  * Used as it simplifies Dom manipulation
  * ['jQuery'](https://api.jquery.com/)


## Testing

Write up for testing is done here: ['Testing documentation'](./testing_doc.md)  

## Deployment

When you clone this repo to cloud9 you will need to create a config.py file which can be placed in the root directory.
And add the following to it.  

```python
DB_CONFIG = {  
    'host': 'your host name',  
    'user': 'user name',  
    'password': 'password',  
    'db':'database name'  
} 

SECRET_KEY = 'your secret key'  
```


For deployment to heroku, you should do the following from cloud9

- Login in to your heroku account using: heroku login
- And then entering you heroku email and password
- Then do: heroku create < name for your website >
- If you do just: heroku create, heroku will create a random name for your website
- If your going to use clearDB database make sure to read notes below
- Then do: git push heroku master

When the push is completed you will see your web address in the console, you can copy and past this into browser to visit your site. Or type in terminal the following: heroku open  

For Database you could use clearDB MySQL database through heroku like I used in this project.  

- After you create your heroku app on heroku you can go to the resources section and add on clearDB.
- Go to setting and click reveal config vars
- You will see CLEARDB_DATABASE_URL which contains all the information you need to connect to the database


I have shown the different parts to the string here : mysql://< DB_USER >:< DB_PASSWORD >@< DB_HOST >/< DB_DB >?reconnect=true  
In config vars add all the configurations.  

DB_USER .. fill in details from string  
DB_PASSWORD ... fill in details from string  
DB_HOST ... fill in details from string  
DB_DB ... fill in details from string  

## Creating database tables

To create the database tables i used MySQL Workbench as it made it easier to visualize the tables and then forward engineered
the tables, copied the print out and adjusted it to get it working with clearDB.  

For those cloning this site you wont need to do this as i have the adjusted file of the print out, you just need to do the following in cloud9 terminal.  

- Get your clearDB database details eg username password host and database name
- In terminal of cloud9 enter: mysql-ctl start 
- This starts mysql 
- Then enter: mysql -h <host> -u<username> -p<password>
- leave a space after the -h  but dont leave a space after the -u and the -p
- Then enter: use <the database name> 
- you are now connected to your database

You are now ready to create the database tables used in the project, and just need to run the file containg the code to create them.  
This is located in a file called create_all.sql.  
To run the file type the following into the ternimal: source create_all.sql; and hit enter  
You should now have all the tables, you can confirm this by tying in the terminal: show tables;
To Exit type in: exit
