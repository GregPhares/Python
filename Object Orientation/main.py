
import re
import csv
import Movie
from Movie import *

###########################################################################
# Functions
###########################################################################
def printMenu(menuItems):
	menuItem = 0
	print("*" * 30)
	for item in menuItems:
		menuItem += 1
		print("%d - %s" % (menuItem, item))
	print("*" * 30)
	return promptForInteger(1, menuItem, 
						    "Please make a selection between 1 and %d:" % menuItem, 
							"Your response must be number between 1 and %d, try again." % menuItem)

def promptForInteger(minimum, maximum, message, errorMessage):
	try:
		response = int(input(message + "\n"))
	except:
		response = -1

	while (response < minimum or response > maximum):
		try:
			response = int(input(errorMessage + "\n"))
		except:
			response = -1
	return response
'''
This loads the scanner, and scans the file filing the movie database
'''
def loadFile(message, movies):
	filename = input(message + "\n")# Input the file being scanned
	file = open(filename, "r") # Opens the file
	lines = list(csv.reader(file)) #Initializes the scanner
	headerCheck=0 # This acts as a counter to skip the document headings
	
	#This uses a foreach loop to scan each element and make each movie object part
	for each in lines:
	   if headerCheck != 0:
	       title = each[0]
	       genre = each[1]
	       director = each[2]
	       writer = each[3]
	       star1 = each[4]
	       star2 = each[5]
	       star3 = each[6]
	       time = each[7]
	       rating = each[8]
	       release = each[9]
	       movies.append(Movie(title,genre, director, writer, star1, star2, star3, time, rating, release))
	   else:
	       headerCheck+=1

'''
Search the movies by title, by using the getter to access each movie object
'''
def searchByTitle(message, movies):
	criteria = input(message + "\n") #Search query
	storage=[] #found object storage
	for movie in movies:
	    title = movie.getTitle() # Gets movie title
	    if criteria.casefold() in title.casefold(): #removes case and checks query against title
	         storage.append(movie)
	         
	return storage
	
'''
Search the movies by genre, by using the getter to access each movie object
'''
def searchByGenre(message, movies):
	criteria = input(message + "\n")
	storage=[]
	for movie in movies:
	    genre = movie.getGenre()# Gets movie genre
	    if criteria.casefold() in genre.casefold(): #removes case and checks query against title
	         storage.append(movie)
	return storage
	
'''
Search the movies by director, by using the getter to access each movie object
'''
def searchByDirector(message, movies):
	criteria = input(message + "\n")
	storage=[]
	for movie in movies:
	    director =movie.getDirector()# Gets movie director
	    if criteria.casefold() in director.casefold(): #removes case and checks query against title
	         storage.append(movie)
	return storage
	
'''
Search the movies by writer, by using the getter to access each movie object
'''
def searchByWriter(message, movies):
	criteria = input(message + "\n")
	storage=[]
	for movie in movies:
	    writer=movie.getWriter()# Gets movie writer
	    if criteria.casefold() in writer.casefold(): #removes case and checks query against title
	         storage.append(movie)
	return storage
	
'''
Search the movies by stars, by using the getter to access each movie object
'''
def searchByStar(message, movies):
	criteria = input(message + "\n")
	storage=[]
	for movie in movies:
	    stars=movie.getStars()# Gets movie stars 
	    if criteria.casefold() in stars.casefold(): #removes case and checks query against title
	         storage.append(movie)
	return storage

'''
Search the movies by run time, by using the getter to access each movie object
'''
def searchByRunningTime(message, movies):
	criteria = input(message + "\n")
	storage=[]
	for movie in movies:
	    time =movie.getTime() # Gets movie run time
	    if int(criteria) > int(time): #removes case and checks query against title
	         storage.append(movie)
	return storage
	
'''
Search the movies by rating, by using the getter to access each movie object
'''
def searchByRating(message, movies):
	criteria = input(message + "\n")
	storage=[]
	for movie in movies:
	    rating=movie.getRating() # Gets movie rating
	    if criteria.casefold() == rating.casefold(): #removes case and checks query against title
	         storage.append(movie)
	return storage
	
'''
Search the movies by release date, by using the getter to access each movie object
'''
def searchByReleaseYear(message, movies):
	criteria = input(message + "\n")
	storage=[]
	for movie in movies:
	    release=movie.getRelease() # Gets movie release date
	    if criteria.casefold() in release.casefold(): #removes case and checks query against title
	         storage.append(movie)
	return storage
	
'''
This will print out the entire movie object
'''
def printMovies(movies):
    movies = sorted(movies, key=lambda movie: movie.getTitle())
    for movie in movies:
	    printin = movie.__str__() #initializes the string print Movie method
	    star = movie.getStars()
	    print(printin)
	    
###########################################################################
# Main
###########################################################################
movies = [ ]

response = 0
while response != 11:
	response = printMenu( [ "Load a Movie File", "Search by Title", "Search by Genre", "Search by Director", \
							"Search by Writer", "Search by Star", "Search by Running Time", \
							"Search by Rating", "Search by Release Year", "Print all Movies", "Quit" ] )
	if response == 1:
		loadFile("Please enter the movie filename: ", movies)
	elif response == 2:
		printMovies(searchByTitle("Please enter the movie title or partial title: ", movies))
		
	elif response == 3:
		printMovies(searchByGenre("Please enter the movie genre or partial genre: ", movies))
		
	elif response == 4:
		printMovies(searchByDirector("Please enter the Director's name or partial name: ", movies))
		
	elif response == 5:
		printMovies(searchByWriter("Please enter the Writer's name or partial name: ", movies))
		
	elif response == 6:
		printMovies(searchByStar("Please enter the Star's name or partial name: ", movies))
		
	elif response == 7:
		printMovies(searchByRunningTime("Please enter the maximum running time in minutes: ", movies))
		
	elif response == 8:
		printMovies(searchByRating("Please enter the movie rating: ", movies))
		
	elif response == 9:
		printMovies(searchByReleaseYear("Please enter the release year: ", movies))
		
	elif response == 10:
		printMovies(sorted(movies, key=lambda movie: movie.getTitle()))
		
	elif response == 11:
		print("Quitting!")
		exit