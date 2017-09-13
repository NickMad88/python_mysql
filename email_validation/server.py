from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    query = "SELECT * from emails"
    friends = mysql.query_db(query)
    
    return render_template('index.html', all_friends=friends)


@app.route('/friends', methods=['POST'])
def create():
    #
    
    # query = "INSERT INTO emails (email, created_at) VALUES (:email, NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'email': request.form['email']
           }
    # Run query, with dictionary values injected into the query.
    # mysql.query_db(query, data)
    query = "SELECT * from emails WHERE :email = email"
    result = mysql.query_db(query, data)
    print result

    return redirect('/')






app.run(debug=True)
