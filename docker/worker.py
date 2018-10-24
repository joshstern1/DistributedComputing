#!/usr/bin/env python

from flask import Flask, request, abort
import os
from werkzeug import secure_filename

app = Flask(__name__)

userfunc = None


@app.route('/', methods=['GET', 'POST'])
def hello():
    return "Hello World"


@app.route('/hello', methods=["GET", "POST"]) #allow both GET and POST requests
def form_example():
    if request.method == "POST": #this block is only entered when the form is submitted
        file = request.files['file']
        file.save(secure_filename(file.filename))
        cmd = "python3 " + file.filename + " > output.txt"
        os.system(cmd)
        with open('output.txt', 'r') as f:
            file_content = f.read()
        return file_content

    return "The post did not work"



app.run(host='0.0.0.0', port=8000)
