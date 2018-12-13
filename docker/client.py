import requests
import os
import sys
import time
#used to simulate the master server, which acts as a client when communicating with docker containers on worker nodes
#sends a post request to a docker container containing a function to be run, then receive and print the function output

sudoPassword = ''

def startup():
    cmd = "python deploy_app.py"
    os.system('echo %s|sudo -S %s' % (sudoPassword, cmd))
    f1 = open("out1.txt", "r")
    IP_ADDR = ""
    for line in f1:
        for char in line:
            if(char != "\n"):
                IP_ADDR = IP_ADDR + char
        break
    f1.close()
    cmd = "rm out1.txt"
    os.system('echo %s|sudo -S %s' % (sudoPassword, cmd))
    return "http://"+IP_ADDR + ":8080"

def shutdown():
    cmd = "python delete_app.py"
    os.system('echo %s|sudo -S %s' % (sudoPassword, cmd))

def main(file_to_run):
    url = startup()
    #url = "http://localhost:8080"
    print(url)
    print("")

    #to send a zip file:
    #fin = open('work.zip', 'rb')

    #to send a file:
    #fin = open('testing.py', 'r')
    #files = {'file': fin}

    try:
        #to send an executable
        data = {'file' : file_to_run}
        r = requests.post(url, data = data)

        #to send a zip file
        #r = requests.post(url = post_url, data = {"mysubmit":"Go"}, files={"archive": ("work.zip", fin)})

        #to send a file:
        #r = requests.post(url, files=files)
        res = ""
        while True:
            res = r.text
            if len(res) > 0:
                break

        print (res)
    finally:
        #fin.close()
        print("")
    shutdown()


text = ""
small_words = open(sys.argv[1]).read().splitlines()
for line in small_words:
    text = text + line
    text += "\n"
main(text)
