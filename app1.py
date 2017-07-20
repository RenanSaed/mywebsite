from flask import Flask, render_template , request
import random
app = Flask(__name__)




@app.route("/")
def home_page():
	return render_template ("index.html")
@app.route("/PHOTOGRAPHIES")
def photographies_page():
	return render_template ("first.html")
@app.route("/WRITINGS")
def writing_page():
	# return render_template("second.html")

	quotes=["an apple a day keeps the doctor away",
	"after clouds,sun shines","better late than never",
	"better safe than sorry","if you want peace be prepared for war"]
	return render_template("index.html",quotes=random.choice(quotes))

@app.route("/CONTACT")
def Contact_page():
	return render_template ("contact.html")
@app.route("/contact_response", methods=["POST"])
def form_res():
	user_firstname =request.form["firstname"]
	user_lastname =request.form["lastname"]
	user_messege =request.form["messege"]
	user_gender =request.form["gender"]

	return  render_template ( "form_data.html", firstname=user_firstname,lastname=user_lastname,messege=user_messege,gender=user_gender)

if __name__=="__main__":
	app.run()






















