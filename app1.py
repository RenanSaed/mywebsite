from flask import Flask, render_template 
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



if __name__=="__main__":
	app.run()






















