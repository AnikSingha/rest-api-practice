from flask import Flask, request
import json

data = json.load(open('data.json', 'r'))

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/', methods = ['GET'])
def home():
    return data

@app.route('/anime', methods = ['GET'])
def anime():
    id = request.args.get('id')
    if id == None:
        return data["anime"]
    elif int(id) > 4999:
        return "<h1>404 Not Found</h1>"
    return data["anime"][f"id: {id}"]

@app.route('/manga', methods = ['GET'])
def manga():
    id = request.args.get('id')
    if id == None:
        return data["manga"]
    elif int(id) > 2550:
        return "<h1>404 Not Found</h1>"
    return data["manga"][f"id: {id}"]

if __name__ == '__main__':
    app.run()