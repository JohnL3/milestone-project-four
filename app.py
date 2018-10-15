import os
import datetime
from flask import Flask, redirect, url_for, render_template, jsonify, request, make_response, g, session
from database.DB_functions import DB_configuration, signup_new_user, validate_user

app = Flask(__name__)
app.config['DEBUG'] = False
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = datetime.timedelta(minutes=10)


mysql = DB_configuration(app)

@app.before_request
def before_request():
    g.user = None
    if 'username' in session:
        g.user = session['username']
        print('before_request', g.user)
    else:
        print('session',session)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        if g.user:
            username = g.user
        else:
            username = None
            '''
            if 'username' in request.args:
                username = request.args['username']
                return render_template('index.html', username=username)
            else:
            '''
            return render_template('index.html', username=username)
        return render_template('index.html', username=username)
    if request.method == 'POST':
       data = request.get_json()
           
       return jsonify({'data':data})

@app.route('/recipe', methods=['GET','POST'])
def recipe():
    if g.user:
        username = g.user
    else:
        username = None
        
    return render_template('recipe.html', username=username)
    
@app.route('/viewrecipe/<recipeid>')
def viewrecipe(recipeid):
    return render_template('viewrecipe.html',id=recipeid)
    
@app.route('/user')
def user():
    if(g.user):
        username= g.user
        return render_template('user.html', username=username)
    else:
        return redirect(url_for('index'))
    
@app.route('/newrecipe', methods=['POST'])
def newrecipe():
    data = request.get_json()
       
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
        username = g.user
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