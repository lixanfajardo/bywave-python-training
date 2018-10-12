_name_ = raw_input("Enter email: ")
_author_ = "lixan@bywave.com.au"

if _name_ == _author_:
	strings = raw_input("Enter Series of strings.\nNOTE: Should be separated by comma(,):\n").replace(" ", "").split(',')
	sortedStrings = ' '.join(sorted(strings))
	print sortedStrings.replace(' ', ', ')
else:
	print "Invalid email. Email is", _author_