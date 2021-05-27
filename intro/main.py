'''
Greg Phares
2/12/2020

This program will help in the learning of interation and looping, "while" introducing boolean statements
that are truthy and falsy. This program will allow for entry of of a list of students, gpa and their number then 
displaying results with quality control. Then this program will allow for the user to enter a number and it convers 
that number to what US change it would be. And finally it is monty pythons and the holy grail scene from the movie
promting the user for answers that are case sensative.

'''
# Part 1
# Prints the intro
print("How many students are in the class?")

number_students = input() # gets the input for the student number

names =[]  # creates a list for the student names

gpa=[] # creates a list for the gpa

student_id = [] #creates a list for student numbers

student_number=0 #a student number counter

# This is the entry point for part 1
if int(number_students)>0:
    
    # this will loop to scan in the names and gpa's of the students if they valid
    for number in range(int(number_students)):
            print("Enter the name of student:")
            name = input() # gets the input for the student name
            student_number+=1 # increments the student number counter
            # this will do the quality check on name, then scan in the users gpa
            if(len(name)<=24):
                print("Enter the gpa of student:")
                each_gpa = float(input()) # scans the gpa for the student 
                
                # does a quality check on gpa, if valid will then store all the information to appropriate lists
                if (each_gpa <= 4.0 and each_gpa>=0.0):
                     names.append(name) # pushes the name in to the names list
                     gpa.append(each_gpa) #adds the gpa to the list
                     
                     student_id.append(student_number) #pushes the student number to the student_id list
                     
                else: 
                     print("GPA of student must be between 0.0 and 4.0.")
            else: 
                print("Name of student cannot exceed 24 characters.")
    
    #Prints the header 
    if len(names)>0:
        print("Number",end =" "*4)
        print("Name",end =" "*20)
        print(end="GPA\n")
        print("-"*37)
        
        # Prints the student's name and gpa
        for student in range(len(names)):
            print(str(student_id[student]),end =" "*9)
            print(str(names[student]), end =" "*(24-len(names[student])))
            print(end=((str(gpa[student]))+"\n"))
            
        sum=0 #sets the sum to 0 to help calc the average
        
        # Iterates through the gpa list to do the first part of a avaerage
        for GPA in range(len(gpa)):
            sum+=gpa[GPA]
        
        # Does a quality check on GPA list, then performs the average calculation and prints it
        if len(gpa)>0:
            print("")
            print("Average GPA: {}".format(float(sum/len(gpa))))

############################################ Part 2 ##############################################
# Entry into part 2, this will allow the user to redo the change making proccess if they so wish 
# Greg Phares
# 2/13/2020
#
# This will create a coint counter that will calc the best change possible for the dollar amount.
# It is will be in the main.
##################################################################################################
def makeChange():
    '''
    This method will count the coins for the from the amount scanned in from the 
    user. This will the parse out each coin amount starting with quarters and working
    its way to pennies.
    '''
    moreChange= True # Boolean to breakout of Part 2
    end = False # Boolean to help end the while loop input check
    noMore = False # Boolean that will be used to end the inner most loop
    quarters= 0 # Will be representing the coin quarter
    nickels = 0  # Will be representing the coin nickel
    dimes= 0 # Will be representing the coin dimes
    pennies = 0 # Will be representing the coin pennies
    
    while end== False:
        print("How much change should the customer get?")
        customer_change="" # Will be use to calc total change, declaring here due to scope 
        customer_change= int(input()) # scans in the change amount from the user to set up the rest of the program
        
        # This will loop ensuring that the user must enter a value above 0
        if customer_change>=0:
            end = True
        else:
            print("Change must be a positive integer")
            
    change_remaining = customer_change  # This is store the remaining change after each coin
    # This will allow for looping process to 
    while noMore == False:
        
        # This will allow to check and calc the number of quarters
        if customer_change>=25:
            quarters = customer_change //25
            change_remaining= customer_change -(quarters*25)
                
        # This will allow to check and calc the number dimes        
        if  change_remaining>=10:
            dimes = change_remaining//10
            change_remaining-=(dimes*10)
        
        # This will allow to check and calc the number of nickels
        if change_remaining >=5:
            nickels = change_remaining//5
            change_remaining-=(nickels*5)
        
        # This will allow to check and calc the number of pennies
        if change_remaining>=1:
            pennies = change_remaining//1
            
        # Prints the header for the the change about to occur
        print("Return the following change:")
        
        # Checks to see if there are quarters to print, if so prints
        if quarters >0:
            print("{} quarters".format(quarters))
            
        # Checks to see if there dimes to print, if so prints
        if dimes > 0:
            print("{} dimes".format(dimes))
            
        # Checks to see if there nickels to print, if so prints
        if nickels >0:
            print("{} nickels".format(nickels))
            
        # Checks to see if there pennies to print, if so prints
        if pennies >0:
            print("{} pennies".format(pennies))
        
        noMore = True   # this breaks out of the cycle to calc coins
        
makeChange() # Calls the method that starts off the 
repeat = True # Boolean for the choice loop
while repeat == True:
     # Prompts the user if they want to exit
    print("Would you like to make more change? (y/Y/n/N)")
    choice = input() # gets the users choice about to exit or not
    #print("User has enter: {}, and with downcase {}".format(choice, choice.lower))
        
    # Checks the users input and then signals to do more change
    if choice=="y" or choice == "Y":
        print("Let's make some more change!")
        makeChange() # calls the method now in the loop if the users
        
    # Checks the users input and then signals them for no more change
    elif choice=="n" or choice=="N":
        print("Ok, I'll move along to something else...")
        repeat = False
            
    else: #This is a catch if erronius entry
        print("I did not recognize that response")


############################################ Part 3 ##############################################
# Entry into part 3, this will ask the user 3 questions and if they are all correct they will be
# allowed access
# Greg Phares
# 2/13/2020
# This will prompt the user to answer 3 questions, if the user gets all three correct they are 
# permited to cross the bridge. But, if they fail they are cast in the cast into the Gorge of 
# Eternal Peril.
##################################################################################################
# This first promps the user

end = False #this will be used to terminate the while loop

# This will allow a infinite loop if the user never gets the answers correct.
while end == False:
    print("Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see.")
    print("What is your name?")
    name = input() # This will get the users entered information for the first questio
    
    # This will check the first question
    if name =="Sir Lancelot of Camelot" or name == "Sir Robin of Camelot" or name == "Sir Galahad of Camelot" or name =="Arthur, King of the Britons":
        print("What is your quest?")
        quest = input() # This will store the information entered from the second question
        
        # This will check the answer provided from the user against the correct answer
        if quest =="To seek the Holy Grail":
            print("What is your favorite color?")
            color = input() # This will store the final information that the user enters for the final question
            
            # This checks the users answer to see if they will be able to cross the bridge
            if color == "Blue" or color == "Yellow":
                print("Right. Off you go.")
                end = True
                
            else: # This is answer for failing question 3
                print("You have been cast into the Gorge of Eternal Peril.  Goodbye.")
        else: # This is the answer for failing question 2
            print("You have been cast into the Gorge of Eternal Peril.  Goodbye.")
    else: #this is the answer for failing question 1
        print("You have been cast into the Gorge of Eternal Peril.  Goodbye.")



    
        