from flask import Flask, Response, send_file, render_template, request, session, make_response, redirect, url_for, flash, g, jsonify
import sys
import atexit

sys.path.append("./docker")
import client

sys.path.append("./database")
from MyDB import MyDB
myDB = MyDB()

flask_app = Flask('flaskapp')
# captain: UserID
flask_app.secret_key = 'thisisatest'
session = {'UserID': 0}

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
		resp = myDB.add_new_user(ID, Pswd)
		if resp == False:
			return jsonify(resp)
		else:
			session['UserID'] = int(resp)
			return jsonify(True)
	else:
		return 'Wrong method'
#    return Response("working on new user block\n", mimetype = 'text/plain')
# To check the credentials
@flask_app.route('/authenticate', methods = ['POST'])
def checkuser():
	if request.method == 'POST':
		ID = request.form['username']
		Pswd = request.form['password']
		resp = myDB.login_user(ID,Pswd)
		if resp == False:
			return jsonify(resp)
		else:
			session['UserID'] = int(resp)
			print(session.get('UserID'))
			print(resp)
			return jsonify(True)
	else:
		return Response('Wrong method \n', mimetype = 'text/plain')

@flask_app.route('/upload', methods = ['POST'])
def upload():
	if request.method == 'POST':
		filename = request.form['file_name']
		file = request.form['file'].encode()
		up = myDB.add_executable(session.get('UserID'), filename, file)
		result = Client.main(file)
		data = {'Flag': True, 'result': result}
		myDB.set_result(up, result)
		return jsonify(data)

@flask_app.route('/run', methods = ['POST'])
def run():
	if request.method == 'POST':
		exec_id = request.form['exec_id']
		file = myDB.get_executable(exec_id)
		result = Client.main(file)
		data = {'Flag': True, 'result': result}
		myDB.set_result(exec_id, result)
		return jsonify(data)

@flask_app.route('/get-executables', methods = ['GET'])
def get_filenames():
	if request.method == 'GET':
		file_list = myDB.get_users_executables(session.get('UserID'))
		return jsonify(file_list)

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
	app.run(threaded=True)