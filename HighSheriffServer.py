import os
from flask import Flask, redirect, request,render_template, jsonify

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

def highSheriffInfo():
    info = "Here is information about the High Sheriff"
    return info

@app.route("/Home", methods=['GET'])
def returnFirst():
    if request.method == 'GET':
        sherifInfo = highSheriffInfo()
        return render_template('home.html', data = sherifInfo)

if __name__ == "__main__":
    app.run(debug=True)
