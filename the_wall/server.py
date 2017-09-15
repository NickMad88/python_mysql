from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import md5
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisisSecret'
mysql = MySQLConnector(app,'thewalldb')

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
        mysql.query_db(query, data)
        # result = mysql.query_db(query, data)
        # print result

    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    
    user_query = "SELECT * FROM users where email = :email AND password = :password"
    query_data = {'email': request.form['email'], 'password': md5.new(request.form['password']).hexdigest()}
    user = mysql.query_db(user_query, query_data)
    if len(user) == 0:
        print "fail"
        return redirect('/')

    session['first_name'] = user[0]['first_name']
    session['user_id'] = user[0]['id']
        # print user

    return redirect('/thewall')


@app.route('/post', methods=['POST'])
def post():
    data = {
                'content': request.form['messagecontent'],
                'user_id': session['user_id'],
                'first_name': session['first_name']
            }
    query = "INSERT INTO messages (content, user_id, created_at) VALUES (:content, :user_id, NOW())"
    mysql.query_db(query, data)

    return redirect('/thewall')

@app.route('/commentpost', methods=['POST'])
def commentpost():
    data = {
                'content': request.form['commentcontent'],
                'user_id': session['user_id'],
                'first_name': session['first_name'],
                'message_id': request.form['commentbutton']
            }
    query = "INSERT INTO comments (content, user_id, message_id, created_at) VALUES (:content, :user_id, :message_id, NOW())"
    print mysql.query_db(query, data)

    return redirect('/thewall')

@app.route('/thewall', methods=['GET'])
def thewall():
    
    displayquery = "SELECT messages.id, users.first_name, messages.user_id, messages.created_at, messages.content FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"
    messages = mysql.query_db(displayquery)
    print "MESSAGES BELOW"
    print messages

    commentdisplayquery = "SELECT comments.message_id, comments.id, comments.content, comments.created_at, users.first_name FROM comments JOIN messages ON comments.message_id = messages.id JOIN users ON comments.user_id = users.id ORDER BY comments.created_at ASC"
    comments = mysql.query_db(commentdisplayquery)
    print "COMMENTS BELOW"
    print comments
    return render_template('thewall.html', all_messages=messages, all_comments=comments)


app.run(debug=True)
