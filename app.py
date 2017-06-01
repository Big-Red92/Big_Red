from flask import Flask, request, render_template, redirect, url_for, session
import smtplib
app = Flask(__name__)


Username=''
Password=''


@app.route('/sent')
def sent():
	Recipient= session['Recipient'] 
	Message =	session['Message'] 
	return render_template("sent.html", Recipient=Recipient, Message=Message)

@app.route('/message', methods=['GET', 'POST'])
def message():
	Username= session['Username']
	print(Username)
	password= session['password']
	print(password)
	if request.method == 'POST':
		
		Recipient= request.form['Recipient']
		print(Recipient)
		Message = request.form['Message']
		print(Message)
		server = smtplib.SMTP('smtp.gmail.com', 587) 
		server.ehlo()
		server.starttls()
		server.ehlo()
		can= True

		try:
			server.login(Username, password)
			
			server.sendmail(Username, Recipient, Message)
			server.quit()
			pass
		except:
			print("wrong input")
			can=False

		while can==False:
			Recipient= request.form['Recipient']
			msg= request.form['Message']
			try:
				server.login(Username, password)
				server.sendmail(Username, Recipient, msg)
				server.quit()
				can= True
				pass
			except:
				print("wrong input")
				can=False
			return render_template("not.html", Username=Username, password=password)

		session['Recipient'] = Recipient
		session['Message'] = Message
		return redirect("/sent")

	return render_template('message.html', Username=Username, password=password)

@app.route('/', methods=['GET', 'POST'])
def send():
	if request.method == 'POST':
		Username = request.form['Username']
		password = request.form['password']
		server = smtplib.SMTP('smtp.gmail.com', 587) 
		server.ehlo()
		server.starttls()
		server.ehlo()
		can = True
		try:
			server.login(Username, password)
			server.quit()
			pass
		except:
			print("invalid Username or Password")
			can = False
		
		while can==False:
			Username = request.form['Username']
			password = request.form['password']
		
			try:
				server.login(Username, password)
				can=True
				server.quit()
				pass
			except:
				print("invalid Username or Password")
				can = False
			return render_template('index2.html')	
		session['Username'] = Username
		session['password'] = password
		return redirect("/message")

	return render_template('index.html')



if __name__ == "__main__":
	app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
	app.run()






