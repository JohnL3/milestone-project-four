import os
import datetime
from flask import Flask, redirect, url_for, render_template, jsonify, request, make_response, g, session
from database.DB_functions import DB_configuration

app = Flask(__name__)
app.config['DEBUG'] = True

mysql = DB_configuration(app)




@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/recipe', methods=['GET','POST'])
def recipe():
    return render_template('recipe.html')

@app.route('/login', methods=['GET','POST'])
def login():
    return 'login'
    
@app.route('/signup', methods=['GET','POST'])
def signup():
    return 'signup'

@app.route('/logout', methods=['GET','POST'])
def logout():
    return 'logout'

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')))