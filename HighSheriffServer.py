import os
from flask import Flask, redirect, request,render_template, jsonify

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

@app.route("/submitApplication", methods=['POST'])
def submitApp():
    if request.method == 'POST':
        return "Application successful"

@app.route("/Home", methods=['GET'])
def returnFirst():
    if request.method == 'GET':
        return render_template('home.html', data = 'Hello World')

@app.route("/Application", methods=['GET'])
def returnApplication():
    if request.method == 'GET':
        return render_template('application.html')

if __name__ == "__main__":
    app.run(debug=True)
