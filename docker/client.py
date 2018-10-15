import requests

url = "http://localhost:8000/hello"
fin = open('testing.py', 'r')
files = {'file': fin}
try:
  r = requests.post(url, files=files)
  print (r.text)
finally:
    fin.close()
