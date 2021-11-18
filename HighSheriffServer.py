import os
from flask import Flask, redirect, request,render_template, jsonify

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


@app.route("/Home", methods=['GET'])
def returnFirst():
    if request.method == 'GET':
        return render_template('home.html', data = 'Hello World')

if __name__ == "__main__":
    app.run(debug=True)
