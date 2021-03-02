from flask import Flask, render_template
from flask import request
import json

app = Flask(__name__)


@app.route('/')
def nesamani():
    with open('./sample-json-file.json') as f:
        data = json.load(f)
    print(data)
    return data

     
if __name__ == "__main__":
    app.run(debug=True,port=3000)    