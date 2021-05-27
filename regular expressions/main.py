import re

###################################################################
# Main
###################################################################

exercise = -1
while (exercise != 0):
	exercise = int(input("Which exercise would you like to test (1-8, 0 to exit)? "))

	#####################################################
	# Exercise 1: Validate Simple Zip Codes
	#####################################################
	if exercise == 1:
		zipcode = input("Enter a zip code: \n")
		check = bool(re.match("\d{5}$",zipcode))
		if check == True:	# TODO: test your search here
			print("Valid")
		else:
			print("Invalid")

	#####################################################
	# Exercise 2: Extended Zip Codes
	#####################################################
	elif exercise == 2:
		zipcode = input("Enter a zip code: \n")
		check = bool(re.match("\d{5}$|\d{5}-\d{4}$",zipcode))
		if check==True:	# TODO: test your search here
			print("Valid")
		else:
			print("Invalid")

	#####################################################
	# Exercise 3: Numerically Correct Zip Codes
	#####################################################
	elif exercise == 3:
		zipcode = input("Enter a zip code: \n")
		check = bool(re.match("\d{1}[1-9]{4}$|\d{1}[1-9]{4}-\d{4}$|[1-9]{1}\d{4}$|[1-9]{1}\d{4}-\d{4}$",zipcode))
		if check == True:	# TODO: test your search here
			print("Valid")
		else:
			print("Invalid")

	#####################################################
	# Exercise 4: Variable Name Validation
	#####################################################
	elif exercise == 4:
		name = input("Enter a variable name: \n")
		check = bool(re.match("[a-z,A-Z_]\d|[a-z,A-Z_]",name))
		if check == True:	# TODO: test your search here
			print("Valid")
		else:
			print("Invalid")

	#####################################################
	# Exercise 5: Username Validation
	#####################################################
	elif exercise == 5:
		username = input("Enter a username: \n")
		check = bool(re.search("^[a-z,A-Z]|^[a-z,A-Z]\w",username))
		if check == True:	# TODO: test your search here
			print("Valid")
		else:
			print("Invalid")

	#####################################################
	# Exercise 6: Min/Max Length Username Validation
	#####################################################
	elif exercise == 6:
		username = input("Enter a username: \n")
		check = bool(re.search("^[a-z,A-Z]{1}\w{5,15}$|^[a-z,A-Z]{1}\w{5,15}$",username))
		if check==True:	# TODO: test your search here
			print("Valid")
		else:
			print("Invalid")

	#####################################################
	# Exercise 7: Email Validator
	#####################################################
	elif exercise == 7:
		email = input("Enter a email address: \n")
		check = re.compile(r"^[a-zA-Z](\.?[\w])*@(([\w])+\.)+[\w]*[\w]{2,4}$")
		if check.search(email):	# TODO: test your search here
			print("Valid")
		else:
			print("Invalid")

	#####################################################
	# Exercise 8: Separate City, State and Zip
	#####################################################
	elif exercise == 8:
		address = input("Enter a city, state and zip: \n")
		check=r"^(?P<City>[A-Z]((([a-z]*)?\.? ?[a-zA-Z]*)*)?)\,\s+(?P<State>[A-Z]{2})\s+(?P<Zip>\d{1}[1-9]{4}$|\d{1}[1-9]{4}-\d{4}$|[1-9]{1}\d{4}$|[1-9]{1}\d{4}-\d{4})$"
		found = re.search(check,address)
		print("City: " +found.group('City'))	# TODO: add the city here
		print("State: "+found.group('State')) # TODO: add the state here
		print("Zip: "+ found.group('Zip')) # TODO: add the zip here

	#####################################################
	# Invalid choice 
	#####################################################
	elif exercise == 0:
		exit

	else:
		print("Your response must be from 0 to 8, try again: ")
