import os
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

def DB_configuration(app):
    '''
    configure database depending on whether debug is set to true or false
    '''
    if app.config['DEBUG'] == True:
        import config
        
        app.config['MYSQL_DATABASE_HOST'] = config.DB_CONFIG['host']
        app.config['MYSQL_DATABASE_PORT'] = 3306
        app.config['MYSQL_DATABASE_USER'] = config.DB_CONFIG['user']
        app.config['MYSQL_DATABASE_PASSWORD'] = config.DB_CONFIG['password']
        app.config['MYSQL_DATABASE_DB'] = config.DB_CONFIG['db']
        
    else:
        app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST')
        app.config['MYSQL_DATABASE_PORT'] = 3306
        app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER')
        app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('DB_PASSWORD')
        app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_DB')
        
    mysql = MySQL(cursorclass=DictCursor)
    mysql.init_app(app)
    return mysql
    
def signup_new_user(mysql, user, pw):
    '''
    Sign up a new user
    '''
    con = mysql.connect()
    curs = con.cursor()
    query = '''SELECT user_name FROM user_table WHERE user_name = "{}" '''
    
    curs.execute(query.format(user))
    result = curs.fetchall()
    
    if result:
        return False
    else:
        try:
            row = (user, pw)
            curs.execute('''INSERT INTO user_table(user_id, user_name, password) VALUES(NULL, %s ,%s)''',row)
            con.commit()
            return True
        except Exception as e:
            return 'Error saving data: '+str(e)

def validate_user(mysql, username, password):
    '''
    Function to try ensure only one person is using a username
    '''
    con = mysql.connect()
    curs = con.cursor()
    query = '''SELECT user_name, password FROM user_table WHERE user_name ="{}" '''

    curs.execute(query.format(username))
    result = curs.fetchall()
    
    if  len(result) != 0:
        if username == result[0]['user_name'] and password == result[0]['password']:
            return True
        else:
            return False
    else:
        return False
        
def get_or_add_author_details(mysql, author_name):
    '''
    Helper function ... gets author id and if author not in table adds author to table and gets id
    '''
    con = mysql.connect()
    curs = con.cursor()
    
    
    curs.execute('''SELECT author_id FROM author_table WHERE author_name = %s''', author_name)
    author_id = curs.fetchall()
    if len(author_id) == 0:
        try:
            curs.execute('''INSERT INTO author_table (author_id, author_name) VALUES (NULL, %s)''', author_name)
            con.commit()
        except Exception as e:
            return 'Author section Error saving data: '+str(e)
        
        curs.execute('''SELECT LAST_INSERT_ID()''')
        author_id = curs.fetchall()
        author_id = author_id[0]['LAST_INSERT_ID()']
        return author_id
    else:
        author_id = author_id[0]['author_id']
        return author_id
        
def get_or_add_category_details(mysql, category_name):
    '''
    Helper function ... get category id and if category is not in table adds it to table then returns id
    '''
    con = mysql.connect()
    curs = con.cursor()
    
    curs.execute('''SELECT cat_id FROM category_table WHERE category_name = %s''', category_name)
    cat_id = curs.fetchall()
    if len(cat_id) == 0:
        try:
            curs.execute('''INSERT INTO category_table (cat_id, category_name) VALUES (NULL, %s)''', category_name)
            con.commit()
        except Exception as e:
            return 'category section Error saving data: '+str(e)
        
        curs.execute('''SELECT LAST_INSERT_ID()''')
        cat_id = curs.fetchall()
        cat_id = cat_id[0]['LAST_INSERT_ID()']
        return cat_id
    else:
        cat_id = cat_id[0]['cat_id']
        return cat_id
        
        
def create_new_recipe(mysql, data):
    con = mysql.connect()
    curs = con.cursor()
    
    username = data['username']
    category = data['category_name']
    author_name = data['author_name']
    
    query = '''SELECT user_id FROM user_table WHERE user_name ="{}" '''
    curs.execute(query.format(username))
    user_id = curs.fetchall()
    user_id = user_id[0]['user_id']
    
    query = '''SELECT author_id FROM author_table WHERE author_name = "{}" '''
    curs.execute(query.format(author_name))
    author_id = curs.fetchall()
    if len(author_id) == 0:
        try:
            name = data['author_name']
            curs.execute('''INSERT INTO author_table (author_id, author_name) VALUES (NULL, %s)''', name)
            con.commit()
        except Exception as e:
            return 'Author section Error saving data: '+str(e)
        
        curs.execute('''SELECT LAST_INSERT_ID()''')
        author_id = curs.fetchall()
        author_id = author_id[0]['LAST_INSERT_ID()']
    else:
        author_id = author_id[0]['author_id']
    
    query = '''SELECT cat_id FROM category_table WHERE category_name = "{}" '''
    curs.execute(query.format(category))
    cat_id = curs.fetchall()
    
    if len(cat_id) == 0:
        try:
            name = data['category_name']
            curs.execute('''INSERT INTO category_table (cat_id, category_name) VALUES (NULL, %s)''', name)
            con.commit()
        except Exception as e:
            return 'Category section Error saving data: '+str(e)
        
        curs.execute('''SELECT LAST_INSERT_ID()''')
        cat_id = curs.fetchall()
        cat_id = cat_id[0]['LAST_INSERT_ID()']
    else:
        cat_id = cat_id[0]['cat_id']
	
	
    Egg = data['allergens'][0]
    Moll = data['allergens'][1]
    Pnuts = data['allergens'][2]
    Nuts = data['allergens'][3]
    SBeans = data['allergens'][4]
    Milk = data['allergens'][5]
    Celery = data['allergens'][6]
    Mustard = data['allergens'][7]
    SSeeds = data['allergens'][8]
    Fish = data['allergens'][9]
    Lupin = data['allergens'][10]
    SDioxide = data['allergens'][11]
    Cerals = data['allergens'][12]
    Crust = data['allergens'][13]
    
    ins = data['instructions']
    prep = data['prep']
    cook = data['cook']
    serves = data['serves']
    url = data['url']
    recipe_name = data['recipe_name']
    
    
    try:
        row = (recipe_name,Nuts,Egg,Milk,Pnuts,Celery,Mustard,SSeeds,Fish,Moll,SBeans,Lupin,SDioxide,Cerals,Crust, ins, 0, 0, prep, cook, serves, url, cat_id, author_id, user_id)
        curs.execute('''INSERT INTO recipe_table(recipe_id, recipe_name, Nuts, Egg, Milk, Pnuts, Celery, Mustard, SSeeds, Fish, Moll, SBeans, Lupin, SDioxide, Cerals, Crust, instructions, likes, collected, prep, cook, serves, url, cat_id, author_id, user_id) VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',row)
        con.commit()
    except Exception as e:
        return 'Recipe section Error saving data: '+str(e)
        
    
    try:
        rows = data['ing_and_quan']
        curs.executemany('''INSERT INTO ingredients_table(recipe_id, ing_name, ing_quantity) VALUES(LAST_INSERT_ID(), %s, %s)''', rows)
        con.commit()
    except Exception as e:
        return ' Ing sect Error saving data: '+str(e)
            
def get_query_string(user):
    '''
    Helper function ... dynamic query string creator 
    '''
    part_g = "user_name, "
    part_h = "JOIN user_table ON recipe_table.user_id = user_table.user_id "
    single_recipe = ',prep, cook, serves, instructions '
    
    part_a = "SELECT "
    part_b = "recipe_name, recipe_id, category_name, author_name, collected, likes, url, "
    part_c = "Nuts, Egg, Milk, Pnuts, Celery, Mustard, SSeeds, Fish, Moll, SBeans, Lupin, SDioxide, Cerals, Crust "
    part_d = "FROM recipe_table "
    part_e = "JOIN author_table ON recipe_table.author_id = author_table.author_id "
    part_f = "JOIN category_table ON recipe_table.cat_id = category_table.cat_id "
    
    if user == 'user':
        full_string = part_a + part_g + part_b +part_c + part_d + part_e + part_f + part_h
    elif user == 'all':
        full_string = part_a + part_b +part_c + part_d + part_e + part_f
    else:
        full_string = part_a + part_b +part_c + single_recipe + part_d + part_e + part_f
    
    return full_string
    
def get_all_recipes(mysql):
    '''
    Get all recipes
    '''
    con = mysql.connect()
    curs = con.cursor()
    
    data = ('recipe_name',
    'recipe_id',
    'category_name',
    'author_name',
    'collected',
    'likes',
    'url',
    'Nuts',
    'Egg',
    'Milk',
    'Pnuts',
    'Celery',
    'Mustard',
    'SSeeds',
    'Fish',
    'Moll',
    'SBeans',
    'Lupin',
    'SDioxide',
    'Cerals',
    'Crust')
    
    query = '''SELECT {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {} FROM recipe_table 
    JOIN author_table ON recipe_table.author_id = author_table.author_id 
    JOIN category_table ON recipe_table.cat_id = category_table.cat_id'''
    
    curs.execute(query.format(*data))
    
    return curs.fetchall()
    
def get_all_user_recipes(mysql, username):
    '''
    get a users recipes
    '''
    con = mysql.connect()
    curs = con.cursor()

    query_a = get_query_string('user')
    query_b = "Where user_name ='"+ username+"'"
    query = query_a + query_b
    
    curs.execute(query)
    return curs.fetchall()
    
def get_single_recipe(mysql, recipe_name):
    '''
    Get a single recipe
    Recipe is contained on two tables
    First query gets main part of recipe
    recipe id is then used to get the ingredients from another table in a second query
    '''
    con = mysql.connect()
    curs = con.cursor()
    recipe = []
    

    query ='''SELECT * FROM recipe_table 
    JOIN author_table ON recipe_table.author_id = author_table.author_id 
    JOIN category_table ON recipe_table.cat_id = category_table.cat_id 
    WHERE recipe_name = "{}" '''
    
    curs.execute(query.format(recipe_name))
    recipe_details = curs.fetchall()
    
    if recipe_details:
        # Get the ingredients used in the recipe 
        
        recipe_id = recipe_details[0]['recipe_id']
    
        ing_query = '''SELECT ing_name, ing_quantity FROM ingredients_table WHERE recipe_id = "{}" '''
    
        curs.execute(ing_query.format(str(recipe_id)))
        recipe_ing = curs.fetchall()
    
        recipe =[recipe_details, recipe_ing]
        return recipe
    else:
        # In case someone uses the ulr bar and types in a recipe name wrong
        return ['No recipe by that name']
    
def user_collects_recipe(mysql, data):
    '''
    add user_id and recipe_id to the user_collects_recipe table in database
    and also updates the value of collected in the recipe_table whre the collected column is
    '''
    
    con = mysql.connect()
    curs = con.cursor()
    
    username = data['user_name']
    recipe_id = data['recipe_id']
    
    # need to get the users user_id 
    curs.execute('''SELECT user_id FROM user_table WHERE user_name = %s''', (username))
    user_id = curs.fetchall()
    user_id = user_id[0]['user_id']
    
    #check if user has allready collected the recipe
    curs.execute('''SELECT user_table_user_id FROM user_collects_recipes WHERE recipe_table_recipe_id = %s and user_table_user_id = %s''', (recipe_id, user_id))
    id_ = curs.fetchall()
    if len(id_) == 0:
        # If the havent then go ahead and insert into table
        try:
            curs.execute('''INSERT INTO user_collects_recipes (user_table_user_id, recipe_table_recipe_id) VALUES(%s, %s)''',(user_id, recipe_id))
            con.commit()
        except Exception as e:
            return ' Insert into user_collects_recipe: '+str(e)
        '''
        Now update collected by 1 in recipe_table collected
        '''
        try:
            curs.execute('''UPDATE recipe_table SET collected = collected +1 WHERE recipe_id = %s''', recipe_id )
            con.commit()
        except Exception as e:
            return ' Updating collected;: '+str(e)
            
        curs.execute('''SELECT collected FROM recipe_table WHERE recipe_id = %s''', recipe_id)
        collected = curs.fetchall()
        collected = collected[0]['collected']
        return collected
    else:
        return 'user allready collected recipe'
  
    
def get_collected_recipes(mysql, username):
    '''
    function for getting all a users collected recipes
    '''
    con = mysql.connect()
    curs = con.cursor()
    
    query = '''SELECT recipe_name, recipe_id, category_name, author_name, collected, likes, url, 
    Nuts, Egg, Milk, Pnuts, Celery, Mustard, SSeeds, Fish, Moll, SBeans, Lupin, SDioxide, Cerals, Crust FROM user_collects_recipes
    JOIN user_table ON user_collects_recipes.user_table_user_id = user_table.user_id 
    JOIN recipe_table ON user_collects_recipes.recipe_table_recipe_id = recipe_table.recipe_id
    JOIN category_table ON recipe_table.cat_id = category_table.cat_id 
    JOIN author_table ON recipe_table.author_id = author_table.author_id
    where user_name = "{}" '''
    
    #query = part_a + part_b + part_c + part_d + part_e
    curs.execute(query.format(username))
    return curs.fetchall()
    
def like_recipe(mysql, data):
    '''
    Function for when user likes a recipe
    '''
    con = mysql.connect()
    curs = con.cursor()
    
    recipe_id = data['recipe_id']
    user_name = data['user_name']
    
    curs.execute('''SELECT COUNT(*) AS count FROM likes WHERE recipe_id = %s AND user_name = %s''', (recipe_id, user_name))
    count = curs.fetchall()
    count = count[0]['count']
    if count == 0:
        try:
            curs.execute('''INSERT INTO likes (user_name, recipe_id) VALUES (%s, %s)''',(user_name, recipe_id));
            con.commit()
        except Exception as e:
            return ' Inserting Likes;: '+str(e)
        
        curs.execute('''SELECT COUNT(*) AS count FROM likes WHERE recipe_id = %s''', (recipe_id))
        count = curs.fetchall()
        count = count[0]['count']
        
        try:
            curs.execute('UPDATE recipe_table SET likes = %s WHERE recipe_id = %s', (count, recipe_id) )
            con.commit()
        except Exception as e:
            return ' Updating likes;: '+str(e)
        
        
        return count
    else:
        return 'You allready Liked this '+str(count)
   

def get_all_authors(mysql):
    '''
    function to get a list of all authors
    '''
    con = mysql.connect()
    curs = con.cursor()
    
    curs.execute('''SELECT author_name FROM author_table''')
    authors = curs.fetchall()
    return authors
    
def get_all_categorys(mysql):
    '''
    function to get a list of categorys
    '''
    con = mysql.connect()
    curs = con.cursor()
    
    curs.execute('''SELECT category_name FROM category_table''')
    categorys = curs.fetchall()
    return categorys
    
def check_what_to_filter_by(data):
    '''
    Helper function used to find out what to filter by
    '''
    if len(data) == 1:
        filter_by = list(data)
       
        return filter_by
    if len(data) == 2:
        filter_by = list(data)
        return filter_by
    else:
        filter_by = list(data)
        return filter_by

def filter_by_category_or_author(mysql, filter_type, val):
    '''
    Helper function to filter by category or author
    '''
    con = mysql.connect()
    curs = con.cursor()
    
    start_str = get_query_string('all')
    end_str = " where "+filter_type+" = '"+val+"' ORDER BY author_name ASC;"
    sql = start_str+end_str
    
    curs.execute(sql)
    return curs.fetchall()

def filter_recipes_by(mysql, data):
    '''
    Get all recipies that dont contain the single allergen or multiple allergens supplied
    '''
    con = mysql.connect()
    curs = con.cursor()
    
    if len(data['allergens']) == 1:
        
        my_list = data['allergens'][0]
        
        my_str = get_query_string('all')
        full_string = my_str +" WHERE "+ my_list + ' !="T" ORDER BY author_name asc'
       
        curs.execute(full_string)
        
        return curs.fetchall()
    else:
        my_list = data['allergens']
        my_str = get_query_string('all')
        mid_str= get_end_str(my_list)
        end_str = " ORDER BY author_name ASC"
        full_string = my_str+mid_str+end_str
        curs.execute(full_string)
        
        return curs.fetchall()
        

def get_end_str(allergens):
    '''
    used to add a && between allergen options eg hasNuts !='T' && hasEgg !='T' 
    '''
    count = len(allergens)
    b_str = " and "
    if len(allergens) == 1:
        my_str = "and " +allergens[0]+ " !='T'"
        return my_str
    else:
        for a in allergens:
            b_str+= a+" !='T'"
            if count > 1:
                b_str+= "&& "
                count-= 1
    return b_str
    

def filter_by_author_and_category(mysql, data):
    '''
    Helper function to filter by aluthor and category
    '''
    con = mysql.connect()
    curs = con.cursor()
    start_str = get_query_string('all')
    
    end_str = " WHERE author_name ='" + data['author_name']+ "' AND category_name ='" + data['category_name']+ "' ORDER BY author_name ASC"
    sql = start_str+end_str
    
    curs.execute(sql)
    return curs.fetchall()
    

def filter_by_allergens_and_author_or_category(mysql, data, item):
    '''
    Helper function to filter by allergen and author or category
    '''
    con = mysql.connect()
    curs = con.cursor()
    start_str = get_query_string('all')
    mid_str = " WHERE "+ item +" ='"+data[item]+"' "
    end_str = get_end_str(data['allergens'])
    end_str += " ORDER BY author_name ASC"
    sql = start_str+mid_str+end_str
    
    curs.execute(sql)
    return curs.fetchall()


def filter_by_all(mysql,data):
    '''
    Helper function to filter by author category and allergen
    '''
    con = mysql.connect()
    curs = con.cursor()
    start_str = get_query_string('all')
    mid_str = " WHERE author_name ='"+data['author_name']+"' AND category_name ='"+data['category_name']+"' "
    end_str = get_end_str(data['allergens'])
    end_str += " ORDER BY author_name asc"
    sql = start_str+mid_str+end_str
    
    curs.execute(sql)
    return curs.fetchall()

def filter_all_recipes(mysql,data):
    '''
    Function to filter all recipes
    '''
    
    items = check_what_to_filter_by(data)
    
    if len(items) == 1:
        if 'author_name' in items or 'category_name' in items:
            result = filter_by_category_or_author(mysql, items[0], data[items[0]])
            return result
        else:
            result = filter_recipes_by(mysql,data)
            return result
        
    if len(items) == 2:
        if 'author_name' in items and 'category_name' in items:
            result = filter_by_author_and_category(mysql,data)
            return result
        elif 'author_name' in items and 'allergens' in items:
            result = filter_by_allergens_and_author_or_category(mysql,data, 'author_name')
            return result
        else:
            result = filter_by_allergens_and_author_or_category(mysql,data, 'category_name')
            return result
    else:
        result = filter_by_all(mysql, data)
        return result
 
        
def set_edit_recipe_update_str(count):
    '''
    Create a dynamic query string
    '''
    
    b_str = "UPDATE recipe_table SET"
    
    y = 1
    for itm in range(count):
        if y != count:
            b_str += " {} = '{}', "
        else: 
            
            b_str += " {} = '{}' WHERE recipe_id = {}"
        y+=1
    
    return b_str
 
    
def update_all_except_ingredients(mysql, data):
    '''
    The non ingredients sections of recipe page are updated by this function
    These are either stored on the recipe_table in database or are a foregin key on the recipe_table
    '''
    con = mysql.connect()
    curs = con.cursor()
    
    update_str=''
    recipe_id = data['zrecipe_id']
    del data['zrecipe_id']
    
    # for author_name and category_name, which i need to update id on recipe_table
    # I first need to check if they are stored in there tables or are new 
    # if new i add them to there table and return id ... if not new i retrive id
    if 'author_name' in data:
            author_name = data['author_name']
            del data['author_name']
           
            data['author_id'] = get_or_add_author_details(mysql, author_name)
            
    if 'category_name' in data:
        category_name = data['category_name']
        del data['category_name']
        
        data['cat_id'] = get_or_add_category_details(mysql, category_name)
            
    count = len(data.items())
    
    # I now have all the info i need and can update recipe_table
    if count > 0:
        update_str = set_edit_recipe_update_str(count)
        
        details =  [itm for sub in data.items() for itm in sub]
        details.append(recipe_id)
        
        try:
            curs.execute(update_str.format(*details));
            con.commit()
            return update_str
        except Exception as e:
            return ' Editing recipe data: '+str(e)
    

def update_ingredients_edit(mysql, ing, r_id):
    '''
    Update ingredients table with edits or add new ingredients to table
    '''
    con = mysql.connect()
    curs = con.cursor()
    
    recipe_id = r_id
    
    if 'old' in ing:
        old_ing =ing['old']
        for itm in old_ing:
            itm.append(recipe_id)
        
        try:
            query ='UPDATE ingredients_table SET ing_name = %s , ing_quantity = %s WHERE ing_name = %s and recipe_id = %s'
            curs.executemany(query,old_ing)
            con.commit()
            return old_ing
        except Exception as e:
                return ' Editing old ingredients: '+str(e) 
        
    if 'new' in ing:
        new_ing = ing['new']
        for itm in new_ing:
            itm.insert(0, recipe_id)
        
        try:
            curs.executemany('''INSERT INTO ingredients_table(recipe_id, ing_name, ing_quantity) VALUES(%s, %s, %s)''', new_ing)
            con.commit()
            return new_ing
        except Exception as e:
            return 'Error saving new_ing: '+str(e)
    
    
    
def edit_single_recipe(mysql, data):
    
    '''
    Edit a single recipe by applying changes to the database
    '''
    
    if 'ing_and_quan' in data:
        ing = {}
        ing = data['ing_and_quan']
        del data['ing_and_quan']
        result = update_ingredients_edit(mysql, ing, data['zrecipe_id'])
        return result
        
        if len(data) > 0:
            result = update_all_except_ingredients(mysql, data)
          
        return result
        
    else:
        '''just update recipe with data'''
        result = update_all_except_ingredients(mysql, data)
      
    return result 
    
   
    
    
    
    
    
    
    
        
    
