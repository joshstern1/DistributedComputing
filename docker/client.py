import requests

#used to simulate the master server, which acts as a client when communicating with docker containers on worker nodes
#sends a post request to a docker container containing a function to be run, then receive and print the function output
 
url = "http://localhost:8000/hello"
fin = open('testing.py', 'r')
files = {'file': fin}
try:
  r = requests.post(url, files=files)
  print (r.text)
finally:
    fin.close()
