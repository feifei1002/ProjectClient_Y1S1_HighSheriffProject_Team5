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

@app.route("/adminDonators", methods = ['GET', 'POST'])
def adminDonators():
	if request.method =='GET':
		return render_template('adminDonators.html')
	if request.method =='POST':
		try:
			surname = request.form.get('surname', default="Error")
			print(surname)
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("SELECT * FROM 'Donators' WHERE surname=?;", [surname])
			data = cur.fetchall()
			print(data)
		except Exception as e:
			print('there was an error')
			print(e)
			conn.close()
			# return "error in adminDonators"
			data=""
		finally:
			conn.close()
			return render_template('ListDonators.html', data = data)


if __name__ == "__main__":
	app.run(debug=True)
