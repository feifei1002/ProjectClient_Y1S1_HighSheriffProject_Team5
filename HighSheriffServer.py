import os
from flask import Flask, redirect, request,render_template, jsonify
import sqlite3

DATABASE = 'HighSheriff.db'
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

@app.route("/adminDonators", methods = ['GET', 'POST'])
def adminDonators():
	if request.method =='GET':
		return render_template('adminDonators.html')
	error = None
	if request.method =='POST':
		if request.form['username']!= 'admin' or request.form['password'] != 'admin':
			error: "Wrong username or password. Please try again."
		else:
			try:
				conn = sqlite3.connect(DATABASE)
				cur = conn.cursor()
				cur.execute("SELECT * FROM 'Donators'")
				data = cur.fetchall()
				print(data)
			except Exception as e:
				print('there was an error')
				print(e)
				conn.close()
				data=""
			finally:
				conn.close()
				return render_template('ListDonators.html', data = data)
if __name__ == "__main__":
	app.run(debug=True)
