import os
from flask import Flask, redirect, request,render_template, jsonify

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


@app.route("/Home", methods=['GET'])
def returnHome():
    if request.method == 'GET':
        sherifInfo = "Here is information about the High Sheriff"
        return render_template('home.html',data=sherifInfo)

@app.route("/nav", methods=['GET'])
def returnnav():
    if request.method == 'GET':
        return render_template('nav.html')

@app.route("/Donations", methods=['GET'])
def returnWork():
    if request.method == 'GET':
        return render_template('Donations.html')

@app.route("/Application", methods=['GET'])
def returnAppplication():
    if request.method == 'GET':
        return render_template('application.html')


if __name__ == "__main__":
    app.run(debug=True)
