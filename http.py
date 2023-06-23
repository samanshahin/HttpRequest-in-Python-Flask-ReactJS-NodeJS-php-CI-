from flask import Flask
from flask import request
from flask import Response
import requests
import urllib
import json

app = Flask(__name__)

@app.route('/')
def index():	# can be 'hello_world' if you type at the address bar 'hello_world'
    return '<h1>Hello, World!</h1>'

@app.route('/secA', methods=['POST', 'GET'], defaults={'name': 'Default'})	# in case of not posting any data
@app.route('/secA/<int:name>', methods=['POST', 'GET'])	# int or string
def secA(name):
    name = request.args.get('name')
    loc = request.args.get('loc')
    return '<h1>Hello {} from {}!</h1>'.format(name, loc)	# in this forms: '/secA?name=your_name&loc=your_location'

@app.route('/urlA')
def get_data():
    return requests.get('http://127.0.0.1:5000/secB?name=john').content

@app.route("/urlB")
def proxy_example():
    r = requests.get("http://127.0.0.1:5000/secB?name=john")
    resp = Response(
        r.text,
        status=r.status_code,
        content_type=r.headers['content-type'],
    )
    return resp.status

@app.route('/secB', methods=['POST', 'GET'], defaults={'name': 'Default'})	# in case of not posting any data
@app.route('/secB/<int:name>', methods=['POST', 'GET'])	# int or string
def secB(name):
    name = request.args.get('name')
    if (name == 'john'):
        name = 'saman'
    return '{}'.format(name)	# in this forms: '/secA?name=your_name&loc=your_location'


if __name__ == '__main__':
    app.run(debug=True)
