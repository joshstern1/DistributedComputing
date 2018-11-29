from flask import Flask, Response, send_file, render_template, request, session, make_response, redirect, url_for, flash, g
import sys
import atexit

sys.path.append("./database")
from MyDB import MyDB
myDB = MyDB()

flask_app = Flask('flaskapp')

@flask_app.route('/')
def main():
    return render_template('main.html')

@flask_app.route('/downloads')
def downloads():
    return render_template('downloads.html')

@flask_app.route('/return-file')
def return_file():
    return send_file('helloworld.c', attachment_filename='hello.c')

# To add new user in the database
@flask_app.route('/new-user', methods = ['POST'])
def adduser():
	if request.method == 'POST':
		ID = request.form['username']
		Pswd = request.form['password']
		return Response(myDB.add_new_user(ID, Pswd))
	else:
		return Response('Wrong method', mimetype = 'text/plain')

# To check the credentials
@flask_app.route('/authenticate', methods = ['POST'])
def checkuser():
	if request.method == 'POST':
		ID = request.form['username']
		Pswd = request.form['password']
		# print(myDB.login_user(ID,Pswd))
		return Response(myDB.login_user(ID, Pswd))
	else:
		return Response('Wrong method \n', mimetype = 'text/plain')

@flask_app.route('/hello')
def hello(name="You"):
    return Response(
        'Josh the goat and ' + name + ' a straight bum!\n',
        mimetype='text/plain'
    )

def closing():
	myDB.close_connection()

atexit.register(closing)

if __name__=='__main__':
	app.run()