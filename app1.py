from flask import Flask, render_template , request
import random
import dataset
app = Flask(__name__)
#db = dataset.connect("postgres://yowahpfaxtsjoc:89e78de430594fa7bffec234ce5bc8ac9193cef0a864378fd900ddd573d65651@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dbn2rcviq5s3i4") 
#table= db["Renan_user"]
#table.insert(dict(name="Renan Sa'ed",age=16,subject="English"))
#print(db.tables)
#table.insert(dict(name="Ishan",age=22,subject="programming"))
#user=table.find_one(name="Renan Sa'ed",age=16 ,subject="English")
#for user in table:
	#print ("Id: "+ str(user["id"])+";name:"+ user["name"]+ user str["age"] +user["subject"])

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
	table.insert(dict(user_firstname=user_firstname,user_lastname=user_lastname,user_messege=user_messege))
#print(db.tables)



	#return  render_template ( "form_data.html", firstname=user_firstname,lastname=user_lastname,messege=user_messege,gender=user_gender)

if __name__=="__main__":
	app.run()






















