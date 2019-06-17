import os
import datetime
from flask import Flask, redirect, url_for, render_template, jsonify, request, make_response, g, session
from database.DB_functions import DB_configuration, signup_new_user, validate_user, create_new_recipe, get_all_recipes, get_all_user_recipes, get_single_recipe, user_collects_recipe, get_collected_recipes, like_recipe, get_all_authors, get_all_categorys, filter_all_recipes, edit_single_recipe
import base64

app = Flask(__name__)


if os.environ.get('C9_HOSTNAME'):
    import config
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = config.SECRET_KEY
else:
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
app.permanent_session_lifetime = datetime.timedelta(days=7)


mysql = DB_configuration(app)


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
    categorys = get_all_categorys(mysql)
    authors = get_all_authors(mysql)
    return render_template('recipe.html', recipe = recipe, username=username, authors=authors, categorys=categorys)

@app.route('/get_all')
def get_all():
    recipe = get_all_recipes(mysql)
    return jsonify(recipe)
    

@app.route('/viewrecipe/<string:recipe_name>')
def viewrecipe(recipe_name):
    if 'username' in session:
        username = session['username']
    else:
        username = None
    # Fetch recipe
    recipe = get_single_recipe(mysql, recipe_name)
    
    if len(recipe) >1:
        # recipe was found make it easier to work with on frontend
        instructions = recipe[0][0]['instructions']
        instructions = instructions.split('_')
        
        ins = []
        for i in instructions:
            ins.append([i])
        recipe[0][0]['instructions'] = ins
        
        return render_template('viewrecipe.html', recipe=recipe[0], recipe_ing=recipe[1], username=username)
    else:
        # Needed incase someone use url bar to manually type in recipe name and spells it wrong
        return render_template('viewrecipe.html', error=recipe[0], username=username)
    
 
@app.route('/user')
def user():
    if 'username' in session:
        username= session['username']
        recipe = get_all_user_recipes(mysql, username)
        categorys = get_all_categorys(mysql)
       
        return render_template('user.html', recipe=recipe, username=username, categorys=categorys)
    else:
        return redirect(url_for('index'))


@app.route('/newrecipe', methods=['POST'])
def newrecipe():
    data = request.get_json()
    
    msg = create_new_recipe(mysql, data)
    data['msg'] = msg
    return jsonify({'data':data})
    
@app.route('/edit_recipe/<recipe_name>', methods=['GET','POST'])
def edit_recipe(recipe_name):
    if 'username' in session:
        if request.method == 'GET':
            data = get_single_recipe(mysql, recipe_name)
        
            return jsonify(data)
        else:
            data = request.get_json()
            edited_recipe = edit_single_recipe(mysql, data)
            return jsonify(edited_recipe)
    else:
        return redirect(url_for('index'))
    
@app.route('/collect', methods=['GET','POST'])
def collect():
    data = request.get_json()
    if 'username' in session:
        username = session['username']
        
        if request.method == 'GET':
            recipes = get_collected_recipes(mysql, username)
           
            return jsonify(recipes)
        else:
            collected = user_collects_recipe(mysql, data)
            return jsonify(collected)
            
@app.route('/likes', methods=['POST'])
def likes():
    if 'username' in session:
        data = request.get_json()
        likes = like_recipe(mysql, data)
        
        return jsonify(likes)
    else:
        return redirect(url_for('signuplogin'))
    
@app.route('/filter_recipes', methods=['POST'])
def filter_recipes():
    data = request.get_json()
    filtered = filter_all_recipes(mysql, data)
    return jsonify(filtered)

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