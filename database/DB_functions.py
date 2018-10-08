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