from flask import Flask, jsonify, send_file
import json
import requests
app = Flask(__name__)


@app.route('/api', methods=['GET','POST'])
def hello_world():
    with open("meta.json",'r') as jsonf:
        return jsonify(json.load(jsonf)), 201

@app.route('/download', methods=['GET','POST'])
def upload():
    path = "README.md"
    return send_file(path, as_attachment=True)

@app.route('/download2', methods=['GET','POST'])
def upload2():
    path = "sampcmd.zip"
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run()
