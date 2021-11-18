import os
from flask import Flask, redirect, request,render_template, jsonify
import sqlite3

DATABASE = 'HighSheriff.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


@app.route("/Home", methods=['GET'])
def returnFirst():
    if request.method == 'GET':
        return render_template('home.html', data = 'Hello World')

@app.route("/adminDonators", method = ['GET', 'POST'])
def adminDonatorsPage():
    if request.method =='GET':
        return render_template('adminDonators.html')
    if request.method =='POST':
        try:
            lastname = request.form.get('lastname', default="Error")
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT * FROM Donators WHERE lastname=?", [lastname])
            data = cur.fetchall()
            print(data)
        except:
            print('there was an error', data)
            conn.close()
        finally:
            conn.close()
            return render_template('adminDonators.html', data = data)


if __name__ == "__main__":
    app.run(debug=True)
