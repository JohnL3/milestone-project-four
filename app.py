import os
import datetime
from flask import Flask, redirect, url_for, render_template, jsonify, request, make_response, g, session
from database.DB_functions import DB_configuration, signup_new_user, validate_user, create_new_recipe, get_all_recipes, get_all_user_recipes


app = Flask(__name__)
app.config['DEBUG'] = True

if app.config['DEBUG'] == False:
   app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
else:
    import config
    app.config['SECRET_KEY'] = config.SECRET_KEY
    
app.permanent_session_lifetime = datetime.timedelta(hours=1)


mysql = DB_configuration(app)
'''
@app.before_request
def before_request():
    g.user = None
    if 'username' in session:
        g.user = session['username']
        print('before_request', g.user)
    else:
        print('session',session)
'''

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        if 'username' in session:
            username = session['username']
        else:
            
            return render_template('index.html')
        return render_template('index.html', username=username)
    if request.method == 'POST':
       data = request.get_json()
           
       return jsonify({'data':data})

@app.route('/recipe', methods=['GET','POST'])
def recipe():
    if 'username' in session:
        username = session['username']
    else:
        username = None
    recipe = get_all_recipes(mysql)
    
    return render_template('recipe.html', recipe = recipe, username=username)
    
@app.route('/viewrecipe/<string:recipe_name>')
def viewrecipe(recipe_name):
    
    return render_template('viewrecipe.html')
 
 
@app.route('/user')
def user():
    if 'username' in session:
        username= session['username']
        
        recipe = get_all_user_recipes(mysql, username)
        
        return render_template('user.html', recipe=recipe, username=username)
    else:
        return redirect(url_for('index'))

@app.route('/newrecipe', methods=['POST'])
def newrecipe():
    data = request.get_json()
    
    msg = create_new_recipe(mysql, data)
    data['msg'] = msg
    return jsonify({'data':data})


@app.route('/signup_login')
def signup_login():
     return render_template('signuplogin.html')
     
    
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = validate_user(mysql, username, password)
        if result == True:
            username = request.form['username']
            session['username'] = username
            return redirect(url_for('user'))
        else:
            return redirect(url_for('signup_login'))
    else:
        if 'username' in session:
            username = session['username']
            return redirect(url_for('user'))
    
    
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    result = signup_new_user(mysql, username, password)
    if result:
        session['username']= username
        return redirect(url_for('login'))
    else:
        return redirect(url_for('signup_login'))

@app.route('/logout', methods=['GET','POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')))