import requests
import os
import deploy_app
#used to simulate the master server, which acts as a client when communicating with docker containers on worker nodes
#sends a post request to a docker container containing a function to be run, then receive and print the function output

sudoPassword = 'BakeJeep10'

def startup():
    cmd = "python deploy_app.py"
    os.system('echo %s|sudo -S %s' % (sudoPassword, cmd))
    f1 = open("out1.txt", "r")
    f2 = open("out2.txt", "r")
    for line in f1:
        NODE_PORT = line
        break
    IP_ADDR = ""
    for line in f2:
        for char in line:
            if(char != "\n"):
                IP_ADDR = IP_ADDR + char
        break
    f1.close()
    f2.close()
    cmd = "rm out1.txt"
    os.system('echo %s|sudo -S %s' % (sudoPassword, cmd))
    cmd = "rm out2.txt"
    os.system('echo %s|sudo -S %s' % (sudoPassword, cmd))
    return "http://"+IP_ADDR + ":" + NODE_PORT

def shutdown():
    cmd = "python delete_app.py"
    os.system('echo %s|sudo -S %s' % (sudoPassword, cmd))

def main():
    url = startup()
    print(url)
    fin = open('testing.py', 'r')
    files = {'file': fin}
    try:
      r = requests.post(url, files=files)
      print (r.text)
    finally:
        fin.close()
    shutdown()
    
if __name__ == '__main__':
    main()
