''' 
Greg Phares
2/7/2020
CS3080
Lab:Python Basics
email: gphares@uccs.edu

This file is designed to help programmers grasp the introduction basics 
of python. Teaching them how to create and declare variables, use input 
and output functions, use different control loops, and how to compare data.
'''

# Output and opperations
a = 248
b = 27
print(str(a+b)) #prints the sum of a and b 
print(str(a-b)) #prints the difference of a and b 
print(str(a*b)) #prints the product of a and b 
print(str(a/b)) #prints the quocient of a and b 
print(str(round(a/b))) #prints the quocient rounded of a and b 
print(str(a%b)) #prints the remainder of a and b 
print(str(pow(a,b))) #prints the power of a to b 
print("*"*67) #Prints 63 of *

#Input
# This will prompt the user to enter a name and it will greet them
print("Please enter your name:")
name = input()
print("Hello, {}".format(name))
print("*"*42) # Prints 42 of *

# Mixing operations
# Prompts the user for 2 int and stores them to a and b
print("Enter two large numerical values:")
a = int(input())
b = int(input())
print("Adding {} + {} = ".format(a,b)+ str(a+b))
print("*"*59)

# Making Decisions
# This test case for a and b, if a is less than. 
if a < b:
     print("{} is not greater than {}".format(a,b))
     # Checks to see if it is even, if so it prints is or is not even
     if a%2 == 0:
         print("{} is even".format(a))
     else: 
         print("{} is not even".format(a))
         
     if b%a ==0: # Checks to see if a is a factor of b, then states result
         print("{} is a factor of {}".format(a,b))
     else:
	       print("{} is not a factor of {} ".format(a,b))
	       
else: # This test case for if b is greater than a then prints it
    print("{} is greater than {}".format(a,b))
    
    # This checks if it is even or not, the prints result
    if a%2 == 0: 
        print("{} is even".format(a))
    else:
        print("{} is not even".format(a))
    # This checks to see if the number is b is a factor of a, then prints result    
    if a%b==0:
        print("{} is a factor of {}".format(b,a))
    else:
	    print("{} is not a factor of {}".format(b,a))
print("*"*26)

#repeated actions
#Prints the header for the user input
print("Enter a small numerical values not equal to 1:")

c = int(input())  # Allows for the storage of the number the user enters
diff = b # This will be used store the number as it is subtracted for the second loop
sum=c # This will be used to store the number while it is being added for the first loop
up = [] # This will be used to store all values of sum after each change is made to sum
down = [] # This will be used to store all values of diff after each change is made to diff

# This will allow for looping of adding items to the up list and self manipulation of sum
while sum <= b:
    up.append(sum)
    sum+=c
# Allows for the manipulated element of sum to be displayed    
for number in up:
    print(number, end = " ")
print("")

# This will allow for the self manipulation of the item diff and the storage of each manipulation
while diff >= c:
    down.append(diff)
    diff-=c
    
# Allows for the manipulated elements of the sum to be displayed
for number in down:
    print(number, end=" ")  
print("")

factors= [] # Stores all values of the number that is being factored
diff=a # This will be used to store the number while it is being added after each iteration
counter=0 # Allows for keeping track of each iteration
prime ="" # This stores the message about the number in question. If or if not prime

# Cycles through each number in range of the entered number
while(diff>=1):
    if a%diff==0:
        storage = a/diff #this saves the number if it is an even division
        
        # This allows for the verification of the number being store is not a duplicate
        if len(factors) ==0:
            factors.append(storage)
        elif factors[counter] == storage:
            counter+=1
        else:
            factors.append(storage)
    diff-=1 # This allows for the investigated number to move down by 1

# This will now check to see if the number is prime after getting all its factors
if int(len(factors))!=2:
    prime = "\n{} is not a prime number"
elif len(factors)==2:
     prime = "\n{} is a prime number"
max = len(factors)-1

# This will print out all the factores and the message if or if not it is a prime
for number in range(max):
        print(int(factors[number]), end = ", ")
print(int(factors[max]), end = "")
print(prime.format(a))






