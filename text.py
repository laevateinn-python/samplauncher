from flask import Flask, jsonify
import json
import requests
app = Flask(__name__)


@app.route('/api', methods=['GET','POST'])
def hello_world():
    with open("meta.json",'r') as jsonf:
        return jsonify(json.load(jsonf)), 201

if __name__ == '__main__':
    app.run()
