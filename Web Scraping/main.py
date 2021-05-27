import os
import requests
import bs4
import time
import datetime

###################################################################
# Main
###################################################################

exercise = -1
while (exercise != 0):
	exercise = int(input("Which exercise would you like to test (1-6, 0 to exit)? "))

	#####################################################
	# Exercise 1:
	#####################################################
	if exercise == 1:
	    result = requests.get('https://automatetheboringstuff.com/files/rj.txt')
	    if (result.status_code == requests.codes.ok):
	        print('Everything is OK')
	    else:
	        print('Something bad happened')
	    print(len(result.text))
	    print(result.text[:47]) 
    
	#####################################################
	# Exercise 2:
	#####################################################
	elif exercise == 2:
	    result = requests.get('https://automatetheboringstuff.com/files/rj.txt')
	    #try:
	    result.raise_for_status()
	    daFile = open("testFile.txt","wb")
	    for stuff in result.iter_content(100000):
	        daFile.write(stuff)
	    
	    daFile.close()
	    file = open("testFile.txt", "r") 
	    storage = file.readlines()
	    file.close()
	    
	    for number in range(50,59+1):
	        print(storage[number],end= '')
	        
	#####################################################
	# Exercise 3:
	#####################################################
	elif exercise == 3:   
	    file = requests.get('http://www.futureme.org/')
	    locate = bs4.BeautifulSoup(file.text, features="html.parser")
	    unit = locate.select('title')
	    print(unit)
	    print(unit[0].getText()) 
    
    
	#####################################################
	# Exercise 4:
	#####################################################
	elif exercise == 4:
	    file = requests.get('http://hmpg.net/')
	    locate = bs4.BeautifulSoup(file.text, features="html.parser")
	    unit = locate.select('p')
	    for p in unit:
	        print("-"*40)
	        print(p)
	        
	    for p in unit:
	        print("-"*40)
	        print(p.getText())
    
	#####################################################
	# Exercise 5:
	#####################################################
	elif exercise == 5:
	    file = requests.get('https://www.daylightofdarkness.com/')
	    locate = bs4.BeautifulSoup(file.text, features="html.parser")
	    unit = locate.select('img')
	    for image in unit:
	        search = image.attrs
	        print(search['src'])
        
	#####################################################
	# Exercise 6:
	#####################################################
	elif exercise == 6:
	    sec = input("How many seconds since Epoch? ")
	    print(time.gmtime(int(sec)))
	    print(time.localtime(int(sec)))
	    storage = datetime.datetime.fromtimestamp(int(sec))
	    print(storage)
	    print(storage.year)
	    print(storage.month)
	    print(storage.hour)
	    original =  datetime.datetime(storage.year, storage.month,storage.day,storage.hour, storage.minute, storage.second)
	    hours = datetime.timedelta(hours = 7)
	    days = datetime.timedelta(days =30)
	    print(original +hours)
	    print(original +days)
	    new = original.strftime("%B %d, %Y")
	    print(new, end= " ")
	    compare = datetime.datetime(2001,9,11,0,0,0)
	    if original< compare:
	        print("is before 9/11")
	    else:
	        print("is after 9/11")
        
            
	#####################################################
	# Invalid choice 
	#####################################################
	elif exercise == 0:
		exit

	else:
		print("Your response must be from 0 to 6, try again: ")
