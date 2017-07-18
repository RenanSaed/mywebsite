from flask import Flask
import random 
app = Flask(__name__)

@app.route("/")
def home_page():
	messege=["hey","i'm Renan Sa'ed","i'm 16","i'd like to get to know you","could you be my friend","would you like to hang out with me"]
	#return"Hello,it's me"

	return random.choice(messege)

@app.route("/photographies")
def my_photos():
	pictures=["flower","seaport","me","we code pics"]

	return random.choice(pictures)
	
@app.route('/')
def load_page() :
	return render_template("index.html")
	
if __name__=="__main__":
    app.run()