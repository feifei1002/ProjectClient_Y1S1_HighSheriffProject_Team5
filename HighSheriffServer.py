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
	# error = None
    # if request.method == 'POST':
    #     if request.form['username'] != 'admin' or request.form['password'] != 'admin':
    #         error = 'Invalid Credentials. Please try again.'
    #     else:
    #         return render_template('moderator.html', variable=quiz_questions[1], num_quest = numNext + 1, list_var = quiz_questions, answer_var = quiz_answers, answervariable=quiz_answers[1])
    # return render_template('login.html', error=error)

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
