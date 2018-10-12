from flask import Flask, Response, send_file, render_template, request, session, make_response, redirect, url_for, flash, g

flask_app = Flask('flaskapp')

@flask_app.route('/')
def main():
    return  render_template('main.html')

@flask_app.route('/downloads')
def downloads():
    return  render_template('downloads.html')

@flask_app.route('/return-file')
def return_file():
    return send_file('/home/joshuastern/Documents/601/DistributedComputing/helloworld.c', attachment_filename='hello.c')

@flask_app.route('/hello')
def hello(name="You"):
    return Response(
        'Josh the goat and ' + name + ' a straight bum!\n',
        mimetype='text/plain'
    )

app = flask_app.wsgi_app
