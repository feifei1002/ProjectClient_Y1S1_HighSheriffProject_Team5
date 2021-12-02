import os
from flask import Flask, redirect, request,render_template, jsonify
from flask.helpers import flash, url_for
from werkzeug.utils import secure_filename
import sqlite3

UPLOAD_FOLDER = '/static/videos'
DATABASE = 'HighSheriff.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def check_filetype(file):
	return '.' in file and \
		file.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS # Checks if the user has submitted a valid file based from our allowed extensions

@app.route("/Application/interactiveForm/filesubmit", methods=['POST'])
def uploadFile():
	if request.method == 'POST':
		if 'file' not in request.files:
			flash('Incorrect file')
			return redirect(request.url) # We should really use redirects instead of returnign strings to users as we have in the past weeks
		file = request.files['file']
		if file.filename == '':
			flash("Empty file has been submitted")
			return redirect(request.url)
		if file and check_filetype(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'].filename))
			return redirect(url_for('download_file', name=filename))

@app.route("/submitApplication", methods=['POST'])
def submitApp():
	if request.method == 'POST':
		email = request.form.get('email', default = "Error")
		firstname = request.form.get('firstname', default = "Error")
		lastname = request.form.get('lastname', default = "Error")
		reason = request.form.get('reason', default = "Error")
		print("inserting applicant"+firstname)
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

@app.route("/generateButtons", methods=['GET'])
def returnButtons():
	if request.method == 'GET':
		return render_template('generateButtons.html')

@app.route("/Application", methods=['GET', 'POST'])
def returnAppplication():
	if request.method == 'GET':
		return render_template('application.html')

@app.route("/Application/interactiveForm", methods=['GET', 'POST'])
def returnAppplication2():
	if request.method == 'GET':
		return render_template('application2.html')

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

    return render_template('admin.html')

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
        ID = request.form.get('ID', default = "Error")
        print("deleting applicant"+ ID)
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

if __name__ == "__main__":
	app.run(debug=True)
