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
    part_h = "JOIN user_table ON recipe_table.user_id = user_table.user_id"
    
    part_a = "SELECT "
    part_b = "recipe_name, recipe_id, category_name, author_name, collected, likes, url "
    part_c = "Nuts, Egg, Milk, Pnuts, Celery, Mustard, SSeeds, Fish, Moll, SBeans, Lupin, SDioxide, Cerals, Crust "
    part_d = "FROM recipe_table "
    part_e = "JOIN author_table ON recipe_table.author_id = author_table.author_id "
    part_f = "JOIN category_table ON recipe_table.cat_id = category_table.cat_id "
    
    if user == 'True':
        full_string = part_a + part_g + part_b +part_c + part_d + part_e + part_f + part_h
    else:
        full_string = part_a + part_b +part_c + part_d + part_e + part_f
    
    return full_string
    
def get_all_recipes(mysql):
    con = mysql.connect()
    curs = con.cursor()
    
    query = get_query_string('False')
    curs.execute(query)
    return curs.fetchall()
    
def get_all_user_recipes(mysql, username):
    con = mysql.connect()
    curs = con.cursor()

    query_a = get_query_string('True')
    query_b = " Where user_name ='"+ username+"'"
    query = query_a + query_b
    
    curs.execute(query)
    return curs.fetchall()
  
    
        
  
    
    
    
    
    
    
    
    
        
    
