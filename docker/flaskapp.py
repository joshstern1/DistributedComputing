from flask import Flask, Response, send_file, render_template, request, session, make_response, redirect, url_for, flash, g
import os

flask_app = Flask('flaskapp')



@flask_app.route('/', methods=['GET', 'POST'])
def hello():
    return Response(
        'Hello World, This is Distributed Computing!\n',
        mimetype='text/plain'
    )

@flask_app.route('/hello', methods=['GET', 'POST'])
def f():

    if request.data:
        data = str(request.data)
        return "Your data was " + data
    else:
        os.system('python3 testing.py > output.txt')
        with open('output.txt', 'r') as f:
            file_content = f.read()
        return file_content

@flask_app.route('/form-example', methods=["GET", "POST"]) #allow both GET and POST requests
def form_example():
    if request.method == "POST": #this block is only entered when the form is submitted
        username = request.form['username']
        password = request.form['password']
        data = "The username is " + username + "and the password is "+password
        return data

    return "The post did not work"

app = flask_app.wsgi_app
