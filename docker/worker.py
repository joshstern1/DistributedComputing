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
    if request.method == "POST": #if a file is uploaded

        #get uploaded file from client (master server)
        file = request.files['file']

        #save the file into the local directory
        file.save(secure_filename(file.filename))

        #execute the file and store the output in output.txt
        cmd = "python3 " + file.filename + " > output.txt"
        os.system(cmd)

        #return the file output to the client (master server)
        with open('output.txt', 'r') as f:
            file_content = f.read()
        return file_content

    return "The post did not work"

app.run(host='0.0.0.0', port=8000)
