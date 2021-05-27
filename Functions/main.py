'''
Greg Phares
2/23/2020
gphares@uccs.edu

This code allows the user to draw using the * to draw different shapes. Also,
it allows for the user to simulate creating a grade book. This grade book allows
for the user to add students, grades, and get to the overall average.
'''
###########################################################################
# Input/Output Functions
'''
This is a menu prompt for when the user first enters the script allowing them to
choose what action they would like to perform
'''
###########################################################################
def menu():
	menuItem = 1
	print("*" * 30)
	print("%d - Draw a Rectangle" % menuItem)
	menuItem = 2
	print("%d - Draw a Right Triangle" % menuItem)
	menuItem = 3
	print("%d - Draw an Isosceles Triangle" % menuItem)
	menuItem =4
	print("%d - Draw a Flipped Isosceles Triangle" % menuItem)
	menuItem =5
	print("%d - Draw a Diamond" % menuItem)
	menuItem =6
	print("%d - Draw an Hourglass" % menuItem)
	menuItem =7
	print("%d - Draw a House" % menuItem)
	menuItem =8 
	print("%d - Add a Student" % menuItem)
	menuItem = 9
	print("%d - Print a Student" % menuItem)
	menuItem = 10
	print("%d - Print all Students" % menuItem)
	menuItem = 11
	print("%d - Quit" % menuItem)
	print("*" * 30)
	return promptForInteger(1, menuItem, 
	        "Please make a selection between 1 and %d:" % menuItem,
	        "Your response must be number between 1 and %d, try again."
	        % menuItem)

'''
This function will act as a prompt for the user. And will be user constantly
in othe methods to print messages and check user input
'''
def promptForInteger(minimum, maximum, message, errorMessage):
    # This will run in a loop allowing for the user to answer questions that are
    # passed to them
    print("{}".format(message))
    while message:
         while True: #boolean as switch case
            try:
                user_input = int(input())
                
                # Prompt the default error that they must use Integers to make
                # a selection
            except ValueError:
                print(end= "Must be an Integer. Try again")
                continue
            else:
                break 
            
         # Gets the user input for the given range        
         if int(user_input) in range(minimum, maximum+1):
            return user_input
         else:
            print(str(errorMessage))
###########################################################################
# Draw Functions
###########################################################################

# This will draw a rectangle in stars
def drawRectangle(width, height):
    
     # This will loop through and print the shape for the *'s
    for draw in range(0, height):
        print("*"*width)

# This will draw a 90 degree triangle
def drawTriangle(size):
    maxCase = 1 # Used to cout the lines 
    
    # This will loop through and print the shape for the *'s
    for draw in range(0,size):
        print("*"*maxCase)
        maxCase+=1

# This will allow for the user to draw a isosceles triangle 
def drawIsoTriangle(size):
    spaces = size-1 # Sets the inicial amount of spaces 
    star =1 # Sets the inicial amount of stars
    
    # This will loop through and print the shape for the given spaces and *'s
    for draw in range(0, size):
        print(" "*spaces,end="")
        print(end ="*"*star)
        print("")
        star+=2 # this will increase the *'s for the next print
        spaces-=1 # this will decrease the *'s for the next print

#  This will allow for the user to draw a upside down isosceles triangle 
def drawUpIsoTri(size):
    stars = (size*2)-1  # Sets the inicial amount of stars
    spaces =0 # Sets the inicial amount of spaces 
    
     # This will loop through and print the shape for the given spaces and *'s
    for draw in range(0,size):
        print(" "*spaces, end ="")
        print(end = "*"*stars)
        print("")
        spaces+=1 # this will increase the *'s for the next print
        stars-=2 # this will decrease the *'s for the next print

def drawTopHrGl(size):
    stars = (size*2)-1 # Sets the inicial amount of stars
    spaces =0  # Sets the inicial amount of stars
    
     # This will loop through and print the shape for the given spaces and *'s
    for draw in range(0,size-1):
        print(" "*spaces, end ="")
        print(end = "*"*stars)
        print("")
        spaces+=1 # this will increase the *'s for the next print
        stars-=2 # this will decrease the *'s for the next print
        
def drawTopDia(size):
    spaces = size-1  # Sets the inicial amount of stars
    star =1 # Sets the inicial amount of stars
    for draw in range(0, size-1):
        print(" "*spaces,end="")
        print(end ="*"*star)
        print("")
        star+=2 # this will increase the *'s for the next print
        spaces-=1 # this will decrees the *'s for the next print

# This will allow to create a dictionary of a student and their grades
def addStudent():
    print("Adding a Student") # Prints out the action to the user
    print("What is the student's name?") # Prompt the user what to type about
    name = input().capitalize() # Gets the user input, caps the first letter
    gradeBookStorage=[] # Creates list to store the grades
    gradeBook ={}  # Creates a dictionary to store the student name & score list
    
    #first prompt to have the user enter the amount of grades for this student
    numberOfGrades = promptForInteger(1,10, 
                    "How many grades does %s have between 1 and 10?" % name, 
                    "You must enter a number between 1 and 10, try again.")
    
    #This will run through the amount specified and get the grades
    for grades in range(0,numberOfGrades):
        grade = promptForInteger(0,100,
                "Enter the student's grade between 0 and 100?",
                "A grade must be between 0 and 100, try again.")
                
        gradeBookStorage.append(grade) # Adds the grades to the list 
    gradeBook[name]=gradeBookStorage # Stores the name & grades as a dictionary
    return gradeBook,name # returns dictionary and list so other methods can use 

# Prints out a single students information
def printStudent(gradeBook,theName):
    print("Print a Student") # Prints out the action to the user
    print("What is the student's name?") # Asks what student the user wants 
    name = input().capitalize() #input of the name being searched for
    
    #this will allow for the dissaembly of the list and dictionary
    if len(theName)!=0:
        theKey=theName.pop(0)
        originate = theName.append(theKey) # refreshes the list of names 
        
        # This will check the name against the dictionary key
        if theKey==name:
           scores = gradeBook.get(theKey)
           print("%s's grades: " % name)
           print("  ",end = ""+str(scores))
           print("")
           sum=0 # This sets the base case for the sum of all the scores
           cloneScores = scores.copy() #creates a copy of the scores to not 
                                       # hurt the original score list
                                       
            # Cycles through the score and adds them all up                         
           for total in range(0,len(scores)):
               grade=cloneScores.pop(0)
               sum+=grade
           average = sum/len(scores) # Cals the average of the scores
           print("  ", end ="Average: {}".format(average)) # Average print out
           print("")
        else:
            print("%s does not exist." % name)
    else:
        print("%s does not exist." % name)
        
# This will allow for the user the option to print out all the student at once
def printAll(classroom, nameList):
    print("Printing all Students") # Prints out the action to the user
    numberOfStudents = len(classroom) # Finding out how many students there are
    currentStudent = sorted(nameList) # Sorts the students alphabetically
    
    # Gets all the students information name and scores
    for students in range(0,numberOfStudents):
        name = currentStudent.pop(0) # Gets the name of the student
        scores = classroom.get(name) # Gets the students scores
        print("%s's grades: " % name) #Prints out the name
        print("  ",end = ""+str(scores)) #Prints out the score
        print("")
        sum=0 # Set the base case for the sum of all scores
        cloneScores=scores.copy() # Copy scores for storage safty
        
        # Creates the sum of all the grades
        for total in range(0,len(scores)):
            grade=cloneScores.pop(0) # Gets the score from the list
            sum+=grade
        average = sum/len(scores)
        print("  ", end ="Average: {}".format(average))
        print("")

###########################################################################
# Handling Functions
###########################################################################

# This Calls all the prompts and method for the needed to draw a Rectangle
def handleRectangle():
   	print("Drawing Rectangle") #Prompt the user rectangle is being drawn
   	# Pompt for the width info
   	width = promptForInteger(1,20, 
   	        "What is the width of your rectangle (1 to 20)?",
   	        "Your width must be between 1 and 20, try again.")
   	
   	# Prompts for the height info
   	height = promptForInteger(1,20,
   	        "What is the height of your rectangle (1 to 20)?",
   	        "Your height must be between 1 and 20, try again.")
   	        
   	# Calls the actual method to do the drawing
   	drawRectangle(width, height)
   	
# This Calls all the prompts and method for the needed to draw a  Right Triangle
def handleTriangle():
    print("Drawing Right Triangle")#Prompt the user triangle is being drawn
    
    # Prompt for the number of rows in the triangle
    size= promptForInteger(1,20, 
        "What is the size of your right triangle (1 to 20)?", 
        "Your size must be between 1 and 20, try again.")
        
    # Calls the method for the triangle
    drawTriangle(size)

# This Calls all the prompts and method for the needed to draw a  Right Triangle
def handleIsoTriangle():
    print("Drawing Isosceles Triangle")
    
    # Prompt for the number of rows in the triangle
    size = promptForInteger(1,20,
            "What is the size of your isosceles triangle (1 to 20)?",
            "Your size must be between 1 and 20, try again.")
            
    # Calls the draw function
    drawIsoTriangle(size)

# This Calls all the prompts and method for the needed to draw a  Right Triangle
def handleUpIsoTri():
    print("Drawing Flipped Isosceles Triangle")
    
    # Prompt for the number of rows in the triangle
    size = promptForInteger(1,20,
        "What is the size of your flipped isosceles triangle (1 to 20)?",
        "Your size must be between 1 and 20, try again.")
    # Calls the draw function
    drawUpIsoTri(size)

# This Calls all the prompts and method for the needed to draw a  Right Triangle    
def handleDiamond():
    print("Drawing Diamond")
    
    # Prompt for longest row number in the diamond
    size = promptForInteger(1,20,
            "What is the size of your diamond (1 to 20)?", 
            "Your size must be between 1 and 20, try again.")

    #calls the method the make the roof, then method to make the house
    drawTopDia(size)
    drawUpIsoTri(size)

# This Calls all the prompts and method for the needed to draw a  Right Triangle    
def handleHourGl():
    print("Drawing Hourglass")# Prompt for the number of rows in the triangle
    
    # Prompt for the the longest row on top and bottum
    size = promptForInteger(1,20,
            "What is the size of your hourglass (1 to 20)?", 
            "Your size must be between 1 and 20, try again.")
            
    # Call method to draw the top then the bottum of the hourglass
    drawTopHrGl(size)
    drawIsoTriangle(size)
 
# This Calls all the prompts and method for the needed to draw a  Right Triangle   
def handleHouse():
    print("Drawing House")# Prints what is occuring
    
    # Prompt for the number of rows in the triangle for roof and hight of house
    size = promptForInteger(1,20,"What is the size of your house (1 to 20)?", 
            "Your size must be between 1 and 20, try again.")
            
    # Calls both functions the make the shape
    drawIsoTriangle(size)
    drawRectangle((size*2)-1,size -1)
    
# This Calls all the prompts and method for the needed to draw a  Right Triangle    
def addStudentHandler(schoolRoom,nameList):
    student,name = addStudent() #calls the method and set the variables
    schoolRoom.update(student) # Updates the student list of names and grades
    nameList.append(name)  # Updates the list of names used as keys
    return schoolRoom


###########################################################################
# Main
'''
This will act as the main in the program. This will respond to what the user
selected what action to perform. This will allow for the proper method to be 
called either a handler or another method
'''
###########################################################################
schoolRoom ={} # Creates the storage for the dictionary of students
nameList=[] # Creates the storage of names that will be used as keys
response = 0
while response != 11:
    response = menu()
    if response == 1:		# Draw Rectangle
        handleRectangle()
        
    elif response == 2:		# Draw Right Triangle
        handleTriangle()   
        
    elif response == 3:		# Draw Isosceles Triangle
        handleIsoTriangle()
        
    elif response == 4:		# Draw Flipped Isosceles Triangle
        handleUpIsoTri()
        
    elif response == 5:		# Draw Diamond
        handleDiamond()
        
    elif response == 6:		# Draw Hourglass
        handleHourGl()
        
    elif response == 7:		# Draw House
        handleHouse()
        
    elif response == 8:		# Add a student
        addStudentHandler(schoolRoom,nameList)

    elif response == 9:		# Print a student
        printStudent(schoolRoom,nameList)
        
    elif response == 10:	# Print all students
        printAll(schoolRoom,nameList)
        
    elif response == 11:	# Quit
        print("Quitting!")
        exit
        
