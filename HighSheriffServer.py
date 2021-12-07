import os
from flask import Flask, redirect, request, render_template, url_for, flash
from werkzeug.utils import secure_filename
import sqlite3

UPLOAD_FOLDER = 'static/uploads/'
DATABASE = 'HighSheriff.db'
ALLOWED_EXTENSIONS = set(['mp4', 'webm'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "MAG355" # Secret key is needed for encryption? Not 100% sure but flask was giving me errors if i didnt set this

def check_filetype(file):
	return '.' in file and \
		file.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS # Checks if the user has submitted a valid file based from our allowed extensions

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

@app.route("/", methods=['GET'])
def returnHome():
	if request.method == 'GET':
		return render_template('home.html')

@app.route("/SherrifInfo", methods=['GET'])
def returnSherrifInfo():
	if request.method == 'GET':
		return render_template('SherrifInfo.html')

@app.route("/SheriffPage", methods=['GET'])
def returnSheriffPage():
	if request.method == 'GET':
		return render_template('SheriffPage.html')

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
		return render_template('generateButtons.html')

@app.route("/Application", methods=['GET', 'POST'])
def returnAppplication():
	if request.method == 'GET':
		return render_template('application.html')

@app.route("/Application/VideoInterview", methods=['GET', 'POST'])
def returnAppplication2():
	if request.method == 'GET':
		return render_template('application2.html')
	if request.method == 'POST':
		if 'file' not in request.files:
			flash('Incorrect file')
			return redirect(request.url) # We should really use redirects instead of returning strings to users as we have in the past weeks
		file = request.files['file']
		if file.filename == '':
			flash("Empty file has been submitted")
			return redirect(request.url)
		if file and check_filetype(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(request.url)

@app.route("/Donations", methods=['GET'])
def returnWork():
	if request.method == 'GET':
		return render_template('Donations.html')


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
			return render_template('adminButtons.html')

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

@app.route("/acceptApplication", methods=['POST'])
def acceptApp():
	if request.method == 'POST':
		ID = request.form.get('ID', default = "Error")
		funds = request.form.get('fundsToAdd', default = "None")
		print("Awarding applicant "+ funds)
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("UPDATE Applicants SET Amount = ? WHERE ID = ?", (funds, ID))

			conn.commit()
			msg = "Application sucessfully accepted"
		except:
			conn.rollback()
			msg = "Error when accepting application"
		finally:
			conn.close()
			return msg
	return render_template('ListApplicants.html')

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


@app.route("/Application/Test", methods=['GET'])
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
