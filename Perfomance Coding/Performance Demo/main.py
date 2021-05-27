
from functools import wraps
from time import time
import functools
'''
Greg Phares
gphares@uccs.edu
3/17/2020
CS3080

This program demonstrates the speed of different formats
in printing, generating, and iterating. Also, this shows
how powerful wrappers can be.
'''

#######################################
# Timing Tools
#######################################

# This will wrap a function and time its star and stop
def timeIt(func):
    @functools.wraps(func) 
    def wrapper(*args,**kwargs):
        start = time() # First timing mark for comparison
        for each in range(0,10000):
           func(*args,**kwargs)
        end = time() # Second timing mark for comparison
        elapse = end -start # Calculating the run time
        elapse *= 1000 #converting to ms
        elapse = format(elapse, '3.3f') #formating the time
        print("{}".format(func.__name__.ljust(20," ")),end =":")
        print("{} ms".format(str(elapse).rjust(10," ")))
        wrapper.name=func.__name__
        return elapse
    return wrapper

# This will take in a list of functions and time them
def timeCompare(list, data):
    times=[] #creating storage of all the performance
    for each in list:
       run = each(data)
       item = [float(run), each.name] #creating each result
       times.append(item)
    times.sort() # Sort the runs from fast to slow
    print("{} is the best".format(times[0][1]))


#######################################
# Test String Concatenation versus Join
#######################################

# This method joins strings together using format
@timeIt
def stringConcatenator(words):
    string ='' #initializing the string
    for each in words: #loop to create string
        string+="{} ".format(each) 

    return string

# This method joins strings using join()
@timeIt
def stringJoiner(words):
    string =" " #initializing string
    string = string.join(words)
    return string

# A collection of words that will be used
# to test Concatenation and Joining
words = []
for i in range(100,300):
    words.append(str(i))

# Calling the compare to get the results Joiner and  Concatenator
timeCompare([stringJoiner,stringConcatenator], words)

print()

#######################################
# Test String Formatting
#######################################

# This method formats the string using %
@timeIt
def stringPercent(words):
    str1 = ""
    for each in words:
        str1 += "%s"%each
   
# This method formats the string using format()
@timeIt
def stringFormat(words):
    str1 = ""
    for each in words:
        str1+="{}".format(each)
    
# This method formats the string using f''
@timeIt
def stringF(words):
    str1 = ""
    for each in words:
        str1+=f"{each}"


# A collection of 13 long strings that will be used to test
# the 3 formatting styles
words = ["Fourscore and seven years ago our fathers brought forth,", 
         "on this continent, a new nation, conceived in liberty,", 
         "and dedicated to the proposition that all men are created equal. ", 
         "Now we are engaged in a great civil war, testing whether that nation,", 
         "or any nation so conceived, and so dedicated, can long endure. ", 
         "We are met on a great battle-field of that war. ", 
         "We have come to dedicate a portion of that field,", 
         "as a final resting-place for those who here gave their lives, "
         "that that nation might live. ", 
         "It is altogether fitting and proper that we should do this. ",
         "But, in a larger sense, we cannot dedicate, ",
         "we cannot consecrate—we cannot hallow—this ground.", 
         "The brave men, living and dead, who struggled here, ",
         "have consecrated it far above our poor power to add or detract. "]


# Use words as the list of words to format
timeCompare([stringPercent,stringFormat, stringF], words)

print()

#######################################
# Test List Building
#######################################

# Creates a interator class to pass a range of numbers
class ListRangeObject:
    # Method that initializes the class
    def __init__(self, n):
        self.n = n
        self.num = 0
    
    def __iter__(self):
      return self

    #This method will pass the next number 
    def __next__(self):
        if self.num < self.n:
           self.num += 1
           return self.num
        else:
            raise StopIteration

# Core of the generator
def rangeGenerator(max):
   num = 0
   while num < max:
       num = num+1
       yield num

# Calls generator using inclusive range format
@timeIt
def listRange(max):
   total = sum(range(1,max+1))
   return total


# Calls generator using list Comprehension format
@timeIt
def listComprehension(max):
   num = [sum(n for n in range(max+1))]
   return num


# Calls the iterator object and returns a number
@timeIt
def listIterator(max):
    num = sum(n for n in ListRangeObject(max))
    return num

# A general call to the generator to return a number
@timeIt
def listGenerator(max):
    num = sum(rangeGenerator(max))
    return num
    
# this method is a generator expression format call
@timeIt
def listExpression(max):
    num = sum(n for n in range(1,max +1))
    return num

max = 100


# Use max as the number of items to generate
timeCompare([listExpression,listRange,listGenerator,listComprehension,listIterator], max)
  
print()
