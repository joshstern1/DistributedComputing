#!/usr/bin/env python

from flask import Flask, request, abort
import os
from werkzeug import secure_filename

app = Flask(__name__)

userfunc = None

@app.route('/', methods=["GET", "POST"]) #allow both GET and POST requests
def hello():
    if request.method == "POST": #if a file is uploaded

        #how to handle executables:

        f1 = open("run_me", "w")
        files = request.form['file']
        for line in files:
            f1.write(line)
        f1.close()
        os.system("chmod 777 run_me")
        os.system("python3 run_me > output.txt")
        with open('output.txt', 'r') as f:
            file_content = f.read()
        os.system("rm output.txt")
        os.system("rm run_me")
        return file_content

        '''
        #how to handle zip files:

        file = request.files['archive']

        #save the file into the local directory
        file.save(secure_filename(file.filename))
        cmd = "unzip " + file.filename
        os.system(cmd)

        os.system("mv work/* .")
        os.system("touch output.txt")
        instructions = open("instructions.txt").read().splitlines()
        for line in instructions:
            cmd = line + " >> output.txt"
            os.system(cmd)

        with open('output.txt', 'r') as f:
            file_content = f.read()
        os.system("rm output.txt")
        os.system("rm instructions.txt")
        os.system("rm -r work")
        os.system("rm work.zip")
        return file_content
        '''


        '''
        #how to handle a python file:
        
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


        '''

    return "The post did not work"


app.run(host='0.0.0.0', port=8080)
