import Shape
import Rectangle
import Triangle

from Shape import *
from Rectangle import *
from Triangle import *

shapes = [ ]
    
###########################################################################
# Input/Output Functions
###########################################################################
def menu():
	menuItem = 1
	print("*" * 30)
	print("%d - Add a Shape" % menuItem)
	menuItem += 1
	print("%d - Add a Rectangle" % menuItem)
	menuItem += 1
	print("%d - Add a Triangle" % menuItem)
	menuItem += 1
	print("%d - Print all Shapes" % menuItem)
	menuItem += 1
	print("%d - Quit" % menuItem)
	print("*" * 30)
	return promptForInteger(1, menuItem, 
						    "Please make a selection between 1 and %d:" % menuItem, 
							"Your response must be number between 1 and %d, try again." % menuItem)

def promptForInteger(minimum, maximum, message, errorMessage):
    value = int(input(message + "\n"))
    while value < minimum or value > maximum:
        value = int(input(message + "\n"))
    return value   # This is stub line to allow the code to run

###########################################################################
# Handling Functions
###########################################################################
def handleShape():
    print("Add a shape")
    theShape = Shape()
    shapes.append(theShape)
    
def handleRectangle():
    print("Add a rectangle")
    height = promptForInteger(1, 20, "Please enter the height between 1 and 20:",
                                    "Your response must be number between 1 and 20:")
    width = promptForInteger(1, 20, "Please enter the width between 1 and 20:",
                                    "Your response must be number between 1 and 20:")
    rectangle = Rectangle(height,width)
    shapes.append(rectangle)

def handleTriangle():
    print("Add a triangle")
    base = promptForInteger(1, 20, "Please enter the base between 1 and 20:",
                                    "Your response must be number between 1 and 20:")
    triangle= Triangle(base)
    shapes.append(triangle)
def handlePrint():
    print("Print all the shapes")
    for shape in shapes:
        shape.draw()
    

###########################################################################
# Main
###########################################################################
response = 0
while response != 5:
    response = menu()
    
    if response == 1:		# Add a Shape
        handleShape()
    elif response == 2:		# Add a Rectangle
        handleRectangle()             
    elif response == 3:		# Add a Triangle
        handleTriangle()            
    elif response == 4:		# Print all the Shapes
        handlePrint()            
    elif response == 5:	# Quit
        print("Quitting!")
        exit