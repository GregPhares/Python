import pprint
###################################################################
# Functions
###################################################################
def PromptForInteger(minValue, maxValue, initialMsg, errorMsg):
    print("{}".format(initialMsg), end = "")
    while initialMsg:
        user_input = input()
        if int(user_input) in range(minValue,maxValue+1):
            return user_input
        else:
            print(end = "{}".format(errorMsg))

def AddNewContact(contactStorage):
    for instance in range(1,6):
        print("Please enter the name of your friend: ", end = " ")
        name = input()
        number =PromptForInteger(100000,9999999,"What is your friend's 7-digit phone number? ", "That's not 7 digits, try again: " )
        contactStorage[name]=number

def AddNewFullContact(storage):
    print("Please enter the name of your friend: ", end="")
    name = input()
    number = PromptForInteger(1000000,9999999, "What is your friend's 7-digit phone number? ", "That's not 7 digits, try again: ")
    print("What is your friend's email address? ", end="")
    email=input()
    age = PromptForInteger(0,125,"What is your friend's age? ", "That's not a real age, try again: ")
    storage[name]={'number':number, 'email':email, 'age': age}
###################################################################
# Main
###################################################################

exercise = -1
while (exercise != 0):
	exercise = int(input("Which exercise would you like to test (1-8, 0 to exit)? "))

	#####################################################
	# Exercise 1: Prompt for Integer
	#####################################################
	if exercise == 1:
		print("Running exercise " + str(exercise))
		print(PromptForInteger(1,100,"Please enter an integer (1 to 100): ","Your response must be from 1 to 100, try again: "))

	#####################################################
	# Exercise 2: Custom Range
	#####################################################
	elif exercise == 2:
		print("Running exercise " + str(exercise))
		print(PromptForInteger(-50, 50, "Please enter an integer (-50 to 50): ", "Your response must be from -50 to 50, try again: "))
		print(PromptForInteger(98, 106, "Please enter your temperature (98 to 106): ", "You must be dead, try again (98 to 106): "))
		print(PromptForInteger(-25, -1, "Please enter the deduction from your account (-25 to -1): ", "Your response must be from -25 to -1, try again: "))
		print(PromptForInteger(1, 10, "Please enter a menu selection (1 to 10): ", "You must choose 1 to 10, try again: "))

	#####################################################
	# Exercise 3: Modifying the Exercise Loop
	#####################################################
	elif exercise == 3:
		print("Running exercise " + str(exercise))

	#####################################################
	# Exercise 4: Simple Lists
	#####################################################
	elif exercise == 4:
		print("Running exercise " + str(exercise))
		itemList = ["Wallet", "Phone","Keys"]
		print(itemList)
		itemList.sort()
		print(itemList)
		print(itemList[0])
		print(itemList[1:])
		print(itemList[-1])
		print(itemList.index("Keys"))
		itemList.append("Tablet")
		print(itemList)
		itemList.insert(1,"Glasses")
		print(itemList)
		itemList.remove("Phone")
		print(itemList)
		itemList.reverse()
		print(itemList)

	#####################################################
	# Exercise 5: Display List Elements on Demand and Copying Lists
	#####################################################
	elif exercise == 5:
		print("Running exercise " + str(exercise))
		theList = ["Stan", "Cartman", "Butters", "Kyle", "Kenny"]
		for count,element in enumerate(theList,0):
		    print(count, element)
		listElement = PromptForInteger(0, len(theList)-1, "Choose a name from the list by number: ", "You must choose one of the above numbers, try again: ")
		print(end ="")
		print("You chose name {}".format(theList[int(listElement)]))
		copiedList = list(theList)
		print(copiedList)
		theList.remove("Cartman")
		print(theList)
		print(copiedList)
		copiedList.remove("Kenny")
		print(theList)
		print(copiedList)
	    
	#####################################################
	# Exercise 6: Summation
	#####################################################
	elif exercise == 6:
		print("Running exercise " + str(exercise))
		end = False
		numberStorage = []
		cycleCounter =0
		while end ==False:
		    numberAmount = PromptForInteger(1,100, "Please enter an integer (1 to 100): ", "Your response must be from 1 to 100, try again: ")
		    print(end = "")
		    numberStorage.append(int(numberAmount))
		    cycleCounter +=1
		    print(end = "")
		    if cycleCounter == 10:
		        end = True
		print(numberStorage)
		total = sum(numberStorage)
		print(total)
		
	#####################################################
	# Exercise 7: Simple Dictionary
	#####################################################
	elif exercise == 7:
		print("Running exercise " + str(exercise))
		contactStorage = {}
		AddNewContact(contactStorage)
		pprint.pprint(contactStorage)
		print(contactStorage.keys())
		print(contactStorage.values())
		print('')
		print("Whose number do you want? ", end =" ")
		query = input()
		print(contactStorage[query])
	#####################################################
	# Exercise 8: Nested Dictionaries
	#####################################################
	elif exercise == 8:
		print("Running exercise " + str(exercise))
		stockerInfo = {}
		for person in range(1,6):
		    AddNewFullContact(stockerInfo)
		pprint.pprint(stockerInfo)
		print(stockerInfo.keys())
		print(stockerInfo.values())
		print("Whose number do you want?", end = " ")
		query = input()
		pprint.pprint(stockerInfo[query])
		print(stockerInfo[query]['email'])
	#####################################################
	# Invalid choice 
	#####################################################
	elif exercise == 0:
		exit

	else:
		print( "Your response must be from 0 to 8, try again: ")
