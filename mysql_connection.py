import psycopg2
import os
from flask import Flask, render_template, request
from mysql.connector import connection
app = Flask(__name__)

config = {}
config['host'] = 'localhost'
config['user'] = 'root'
config['password'] = 'Sandeep007'
config['database'] = 'badminton_court_booking'

DATABASE_URL = os.environ.get("DATABASE_URL")
mysql = psycopg2.connect(DATABASE_URL)
mysql.autocommit = True

@app.route('/signup', methods=['POST'])
def register():
    details = request.json
    Name = details['name']
    email = details['email']
    password = details['passwd']
    phone = details['phn']
    cur = mysql.cursor()
    cur.execute("INSERT INTO user_details(user_name, email,password,phone) VALUES (%s, %s, %s, %s)", (Name, email, password, phone))
    # mysql.commit()
    cur.close()
    return 'success'

@app.route('/login', methods=['POST'])
def login():
 
    details = request.json
    Name = details['name']
    password = details['passwd']
    cur = mysql.cursor()
    cur.execute("""SELECT user_name,password FROM user_details where user_name = '%s' and password = '%s' """%(Name,password))
    myresult = cur.fetchall()
    cur.close()
    if (myresult == []):
       print("Wrong")
       return 'failure', 404
    else:
       print("Correct")
       return 'success'

@app.route('/details',methods=['POST'])
def details():
	details = request.json
	Name = details['name']
	bid = details['booking_id']
	time = details['time']
	court_type = details['court']
	cur = mysql.cursor()
	cur.execute("INSERT INTO booking_details(user_name,booking_id,timing,court_type) VALUES (%s, %s, %s, %s)", (Name,bid,time,court_type))
	#mysql.commit()
	cur.close()
	return 'success'	
    

if __name__ == '__main__':
    app.run("0.0.0.0")