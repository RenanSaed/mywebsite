def create_dict():
	subjects_dict={

	"Arabic" : "Mohammed",
	"English" : "Baher",
	"programming": "ishan",
	"design thinking": "jessie",
	}
	return subjects_dict

def print_output(subjects,subject): #subjects value #subject key
	print subject+" was taught by "+subjects[subject] #subjects[subject] is the value #subject is key
	 #print "English was taught by"+" "+subjects["English"]
	 # print "Arabic was taught by"+" "+subjects["Arabic"]




def main(): 
	dictionary=create_dict()
	#for subject in dictionary:
	subject= raw_input("choose your subject to know the teacher or enter to quite" )
	while (subject!=""):
		if subject in dictionary :
			print_output(dictionary, subject)
		else:
			print ("no subject found")
		subject= raw_input("choose your subject to know the teacher or enter to quite" )









if __name__=="__main__":
	main()