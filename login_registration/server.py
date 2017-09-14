from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import md5
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisisSecret'
mysql = MySQLConnector(app,'loginregdb')

@app.route('/')
def index():

    
     return render_template('index.html')


@app.route('/register', methods=['POST'])
def create():
    valid = 'true'
    if len(request.form['first_name']) < 1:
        flash("You must enter in valid first name")
        valid = 'false'
    if len(request.form['last_name']) < 1:
        flash("You must enter in valid last name")
        valid = 'false'
    if len(request.form['email']) < 1:
        flash("You must enter in valid email")
        valid = 'false'
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address!")
    if len(request.form['password']) < 8:
        flash('Password must be 8 characters at minimum')
        valid = 'false'

    password = request.form['password']
    repassword = request.form['repassword']

    if repassword != password:
        flash('Passwords do not match!')
        valid = 'false'
   
    if valid == 'true':
        query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (:first_name, :last_name, :email, :password, NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'password': md5.new(request.form['password']).hexdigest()
            }
        # Run query, with dictionary values injected into the query.
        # mysql.query_db(query, data)
        result = mysql.query_db(query, data)
        print result

    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    
    user_query = "SELECT * FROM users where email = :email AND password = :password"
    query_data = {'email': request.form['email'], 'password': md5.new(request.form['password']).hexdigest()}
    user = mysql.query_db(user_query, query_data)
    print user
    if len(user) > 0:
       flash("logged in")
       print "success"
    else:
        print "fail"
    return render_template('index.html')



app.run(debug=True)
