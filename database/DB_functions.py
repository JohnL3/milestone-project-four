import os
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

def DB_configuration(app):
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
    con = mysql.connect()
    curs = con.cursor()
    query = "SELECT user_name FROM user_table WHERE user_name ='" +user+ "'"
    
    curs.execute(query)
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
    con = mysql.connect()
    curs = con.cursor()
    query = "SELECT user_name, password FROM user_table WHERE user_name ='" +username+ "'"

    curs.execute(query)
    result = curs.fetchall()
    
    if  len(result) != 0:
        if username == result[0]['user_name'] and password == result[0]['password']:
            return True
        else:
            return False
    else:
        return False
        
def create_new_recipe(mysql, data):
    con = mysql.connect()
    curs = con.cursor()
    
    username = data['username']
    category = data['category_name']
    
    query = "SELECT user_id FROM user_table WHERE user_name ='" +username+ "'"
    curs.execute(query)
    user_id = curs.fetchall()
    user_id = user_id[0]['user_id']
    
    query = "SELECT author_id FROM author_table WHERE author_name ='" +data['author_name']+ "'"
    curs.execute(query)
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
    
    query = "SELECT cat_id FROM category_table WHERE category_name ='" +category+ "'"
    curs.execute(query)
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
    con = mysql.connect()
    curs = con.cursor()
    
    query = get_query_string('all')
    curs.execute(query)
    return curs.fetchall()
    
def get_all_user_recipes(mysql, username):
    con = mysql.connect()
    curs = con.cursor()

    query_a = get_query_string('user')
    query_b = "Where user_name ='"+ username+"'"
    query = query_a + query_b
    
    curs.execute(query)
    return curs.fetchall()
    
def get_single_recipe(mysql, recipe_name):
    con = mysql.connect()
    curs = con.cursor()
    recipe = []
    
    query_a = get_query_string('single')
    query_b = "WHERE recipe_name ='"+ recipe_name +"'"
    query = query_a + query_b
    
    curs.execute(query)
    recipe_details = curs.fetchall()
    
    recipe_id = recipe_details[0]['recipe_id']
    
    ing_query = "SELECT ing_name, ing_quantity FROM ingredients_table WHERE recipe_id = " + str(recipe_id) 
    
    curs.execute(ing_query)
    recipe_ing = curs.fetchall()
    
    recipe =[recipe_details, recipe_ing]
    return recipe
    
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
    con = mysql.connect()
    curs = con.cursor()
    
    part_a = "SELECT recipe_name, recipe_id, category_name, author_name, collected, likes, url, "
    part_b = "Nuts, Egg, Milk, Pnuts, Celery, Mustard, SSeeds, Fish, Moll, SBeans, Lupin, SDioxide, Cerals, Crust FROM user_collects_recipes "
    part_c = "JOIN user_table ON user_collects_recipes.user_table_user_id = user_table.user_id JOIN recipe_table ON user_collects_recipes.recipe_table_recipe_id = recipe_table.recipe_id "
    part_d = "JOIN category_table ON recipe_table.cat_id = category_table.cat_id JOIN author_table ON recipe_table.author_id = author_table.author_id "
    part_e = " where user_name ='"+ username +"'"
    
    query = part_a + part_b + part_c + part_d + part_e
    curs.execute(query)
    return curs.fetchall()
    
def like_recipe(mysql, data):
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
    con = mysql.connect()
    curs = con.cursor()
    
    curs.execute('''SELECT author_name FROM author_table''')
    authors = curs.fetchall()
    return authors
    
def get_all_categorys(mysql):
    con = mysql.connect()
    curs = con.cursor()
    
    curs.execute('''SELECT category_name FROM category_table''')
    categorys = curs.fetchall()
    return categorys
    
def check_what_to_filter_by(data):
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
    con = mysql.connect()
    curs = con.cursor()
    
    start_str = get_query_string('all')
    end_str = " where "+filter_type+" = '"+val+"' ORDER BY author_name ASC;"
    sql = start_str+end_str
    
    curs.execute(sql)
    return curs.fetchall()

def filter_all_recipes(mysql,data):
    items = check_what_to_filter_by(data)
    
    if len(items) == 1:
        if 'author_name' in items or 'category_name' in items:
            result = filter_by_category_or_author(mysql, items[0], data[items[0]])
            return result
    
   
    
    
    
    
    
    
    
        
    
