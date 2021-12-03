import os
from flask import Flask, redirect, request,render_template, jsonify
import sqlite3

DATABASE = 'HighSheriff.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

@app.route("/submitApplication", methods=['POST'])
def submitApp():
	if request.method == 'POST':
		email = request.form.get('email', default = "Error")
		firstname = request.form.get('firstname', default = "Error")
		lastname = request.form.get('lastname', default = "Error")
		reason = request.form.get('reason', default = "Error")
		print("inserting applicant "+firstname)
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("INSERT INTO Applicants ('firstName', 'surName', 'Email', 'Reason')\
						VALUES (?,?,?,?)",(firstname, lastname, email, reason) )

			conn.commit()
			msg = "Record successfully added"
		except:
			conn.rollback()
			msg = "error in insert operation"
		finally:
			conn.close()
			return msg

@app.route("/Home", methods=['GET'])
def returnHome():
	if request.method == 'GET':
		return render_template('home.html')

@app.route("/SherrifInfo", methods=['GET'])
def returnSherrifInfo():
	if request.method == 'GET':
		return render_template('SherrifInfo.html')

@app.route("/SherrifPage", methods=['GET'])
def returnSherrifPage():
	if request.method == 'GET':
		return render_template('SherrifPage.html')

@app.route("/WebsiteInfo", methods=['GET'])
def returnWebsite():
	if request.method == 'GET':
		return render_template('WebsiteInfo.html')

@app.route("/nav", methods=['GET'])
def returnnav():
	if request.method == 'GET':
		return render_template('nav.html')

@app.route("/dropdown", methods=['GET'])
def returndropdown():
	if request.method == 'GET':
		return render_template('dropdown.html')

@app.route("/boostrap", methods=['GET'])
def returnBoostrap():
	if request.method == 'GET':
		return render_template('boostrap.html')

@app.route("/Application", methods=['GET', 'POST'])
def returnAppplication():
	if request.method == 'GET':
		return render_template('application.html')


@app.route("/Charities", methods =['GET'])
def returnCharities():
	if request.method == 'GET':
		return render_template('charities.html')


@app.route("/admin", methods = ['GET', 'POST'])
def admin():
	if request.method =='GET':
		return render_template('admin.html')
	error = None
	if request.method =='POST':
		if request.form['username']!= 'admin' or request.form['password'] != 'admin':
			error = "Wrong username or password. Please try again."
			print(error)
			return render_template('admin.html')
		else:
			return render_template('2buttons.html')

	return render_template('admin.html')

@app.route("/ListApplicants", methods=['GET'])
def listApplicants():
	if request.method =='GET':
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("SELECT * FROM 'Applicants'")
			data = cur.fetchall()
			print(data)
		except Exception as e:
			print('there was an error')
			print(e)
			conn.close()
			data=""
		finally:
			conn.close()
			return render_template('ListApplicants.html', data = data)

@app.route("/declineApplication", methods=['POST'])
def declineApp():
	if request.method == 'POST':
		ID = request.form.get('decline', default = "Error")
		print("deleting applicant "+ ID)
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("DELETE FROM Applicants WHERE ID = ?", (ID))

			conn.commit()
			msg = "Application successfully deleted"
		except:
			conn.rollback()
			msg = "error in decline application"
		finally:
			conn.close()
			return msg
	return render_template('ListApplicants.html')

@app.route("/ListTests", methods=['GET'])
def listQuestions():
	if request.method =='GET':
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("SELECT * FROM 'Tests'")
			data = cur.fetchall()
			print(data)
		except Exception as e:
			print('there was an error')
			print(e)
			conn.close()
			data=""
		finally:
			conn.close()
			return render_template('ListTests.html', data = data)

@app.route("/addTest", methods=['POST'])
def addTest():
	if request.method == 'POST':
		add = request.form.get('add', default = "Error")
		answer = request.form.get('option', default="Error")
		print("adding question " + add)
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("INSERT INTO Tests ('Test', 'Answer') VALUES (?,?)", [add, answer])
			conn.commit()
			msg = "Test successfully added"
		except Exception as e:
			print('there was an error')
			print(e)
			conn.rollback()
			msg = "error in adding test"
		finally:
			conn.close()
			return msg
	return render_template('ListTests.html')

@app.route("/deleteTest", methods=['POST'])
def deleteQuestion():
	if request.method == 'POST':
		delete = request.form.get('delete', default = "Error")
		print("deleting question " + delete)
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("DELETE FROM Tests WHERE ID = ?", (delete))
			conn.commit()
			msg = "Test successfully deleted"
		except Exception as e:
			print('there was an error')
			print(e)
			conn.rollback()
			msg = "error in deleting test"
		finally:
			conn.close()
			return msg
	return render_template('ListTests.html')


@app.route("/Tests", methods=['GET'])
def reworkingTests():
	if request.method =='GET':
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("SELECT ID, Test FROM 'Tests'")
			data = cur.fetchall()
			print(data)
		except Exception as e:
			print('there was an error')
			print(e)
			conn.close()
			data=""
		finally:
			conn.close()
			return render_template('reworkingTests.html', data = data)

@app.route("/submitTest", methods =['POST'])
def submitTest():
	if request.method == 'POST':
		email = request.form.get('email', default = "Error")
		firstname = request.form.get('firstname', default = "Error")
		lastname = request.form.get('lastname', default = "Error")
		score = request.form.get('score', default = "Error")
		print("inserting applicant "+firstname)
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("INSERT INTO reworkingApplicants ('firstName', 'surName', 'Email', 'Score')\
						VALUES (?,?,?,?)",(firstname, lastname, email, score) )
			conn.commit()
			msg = "Record successfully added"
		except Exception as e:
			print('there was an error')
			print(e)
			conn.rollback()
			msg = "error in insert operation"
		finally:
			conn.close()
			return msg

@app.route("/ListreworkingApplicants", methods=['GET'])
def listreworkingApplicants():
	if request.method =='GET':
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("SELECT * FROM 'reworkingApplicants'")
			data = cur.fetchall()
			print(data)
		except Exception as e:
			print('there was an error')
			print(e)
			conn.close()
			data=""
		finally:
			conn.close()
			return render_template('ListreworkingApplicants.html', data = data)

if __name__ == "__main__":
	app.run(debug=True)
