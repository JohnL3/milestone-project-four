import os
import datetime
from flask import Flask, redirect, url_for, render_template, jsonify, request, make_response, g, session
from database.DB_functions import DB_configuration

app = Flask(__name__)
app.config['DEBUG'] = True

mysql = DB_configuration(app)




@app.route('/', methods=['GET','POST'])
def index():
    return 'All Good'
    

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')))