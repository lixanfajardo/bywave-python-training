_name_ = raw_input("Enter email: ")
_author_ = "lixan@bywave.com.au"
if _name_ == _author_:
	number = raw_input("Enter number from 60 upto 100: ")
	try:
		number = int(number)
		if number in range(60, 101):
			#print "Number is greater than 60 continue logic"
			if number in range(60, 75):
				print "Derp"
			elif number in range(75, 85):
				print "Good"
			elif number in range(85, 95):
				print "Very Good"
			elif number in range(95, 101):
				print "Level Asian!"
		else:
			print "Invalid value. Number must be greater than 60"
	except ValueError:
		print "Number must be an integer. Must be more than 60 and less than 100"
else:
	print "Invalid email. Email is", _author_
#print _author_




