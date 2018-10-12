# This is the basic hello world server
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'HEAD', 'OPTIONS', 'PUT', 'DELETE'])
def F():
	if request.data:
		name = request.get_json()["name"]
	else:
		name = "World"
	return 'Hello '+name+' !'

if __name__=='__main__':
	app.run(host='0.0.0.0', port=5000)
