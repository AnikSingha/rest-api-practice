from flask import Flask, request
import json

data = json.load(open('data.json', 'r'))

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/', methods = ['GET'])
def home():
    id = request.args.get('id')
    if id == None:
        return data
    elif int(id) > 1000:
        return "<h1>404 Not Found</h1>"
    return data[f"id: {id}"]

if __name__ == '__main__':
    app.run()