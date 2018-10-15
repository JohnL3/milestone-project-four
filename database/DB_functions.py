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
        
    
