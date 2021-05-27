# TODO: Build the Movie class here
import re

class Movie:
    '''
    This methods initializes the class allowing it to be used and load the class
    with variables. All variables that are invicialized are python "private"
    '''
    def __init__(self, title, genre, director, writer, star1, star2, star3, runTime, rating, release):
        self.__title=title 
        self.__genre=genre
        self.__director=director
        self.__writer = writer
        self.__star1=star1
        self.__star2=star2
        self.__star3= star3
        self.__runTime=runTime
        self.__rating=rating
        self.__release=release
    
    '''
    This method takes everything and smashes it together in a string as we were
    instructed to do, to one long string can be passed for printing purposes
    '''
    def __str__(self):
        hours = int(self.__runTime) //60 # Converts hours from minutes
        min = int(self.__runTime)%60 # Converts remainder to minutes
        minutes = '{:02d}'.format(min) # Formats the minutes to have 2 digits
        
        moviestr = "-"*80+"\n" # header of the print
        
        '''
        This this will sort and gather the first 3 lines for the print out
        and if the Title is to long it will be split in several lines with over
        items associate on the first 3 lines
        '''
        if len(self.__title)<= 90 and len(self.__title)>55:
            title1 =re.search(r'[\D]{1,55}\s',self.__title) #Regex line 1 title
            title1 = title1.group() #converts the regex to string
            
            #cuts the string of the title and allows for the rest to be printed
            cut = self.__title.replace(title1,'')
            title2 =re.search(r'[\D]{1,35}\s',self.__title)#Regex line 2 title
            title2= cut
            
            # Adding to the string print out for the first 3 lines
            moviestr+=(title1.ljust(55," ")+"  |  "+("{} h {} min".format(hours, minutes)))
            moviestr+=("  |  "+self.__rating.rjust(5,' ')+"\n")#line 1 end
            moviestr+=(title2.ljust(35," ")+"  |  "+"Director: "+str(self.__director)+"\n")
            moviestr+=((" "*35)+"  |  "+"Writer:   "+str(self.__writer)+"\n")
            
        #this checks if the title is larger than 90 characters 
        elif len(self.__title)<= 125 and len(self.__title)>90:
            title1 =re.search(r'^([\D]{1,55})\s',self.__title)#Regex line 1 title
            title1 = title1.group() # Convert Regex to string
            cut1 = self.__title.replace(title1,'') #Removes line 1 from title
            
            title2 =re.search(r'^([\D]{0,35})\s',cut1) #Regex for title line 2
            title2= title2.group() #Convert search to string for title line 2
            cut2 = cut1.replace(title2,'') #Removes line 2 from title, so now line 3

            # Adding to the string print out for the first 3 lines
            moviestr+=(title1.ljust(55," ")+"  |  "+("{} h {} min".format(hours, minutes)))
            moviestr+=("  |  "+self.__rating.rjust(5,' ')+"\n")#line 1 end
            moviestr+=(title2.ljust(35," ")+"  |  "+"Director: "+str(self.__director)+"\n")#not sure if need str() #line 2
            moviestr+=(cut2.ljust(35," ")+"  |  "+"Writer:   "+str(self.__writer)+"\n")#line 3
 
        else: #This will be if the title does not need to be rapped. Then prints first 3 lines
        
           moviestr+=(self.__title.ljust(55," ")+"  |  "+("{} h {} min".format(hours, minutes)))
           moviestr+=("  |  "+self.__rating.rjust(5,' ')+"\n")# line 1 end
           moviestr+=((" "*35)+"  |  "+"Director: "+str(self.__director)+"\n")#line 2 end
           moviestr+=((" "*35)+"  |  "+"Writer:   "+str(self.__writer)+"\n")# line 3 end
           
           
        moviestr+=("Genre:   "+self.__genre+"\n")#Adds line for to print string
        moviestr+=("Stars:   ") #starter of line 5
        
        #Regex for stars for line 5 and if needed line 6
        stars = self.__star1+', '+self.__star2+', '+self.__star3# All the stars
        liner1 = re.search(r'^(.){0,70}\s',stars) # Regex stars line 1
        liner1 = liner1.group()# Convert to string for stars line 1
        snip1 = stars.replace(liner1,'')# Removes line 1 from stars, so now line2
        
        #This will test to see if this needs to be rapped or just added as is
        starLen= len(stars)
        if starLen>71: #If more than 71 characters prints 2 star lines
            moviestr+=liner1+"\n" #line 1 for stars
            moviestr+=(" "*9)+snip1+"\n" # Line 2 of stars
        else:
            moviestr+=stars+"\n" # Not rapped line of stars
        
        '''
        This section will convert the date from just numbers to typed for of a 
        date.
        '''
        moviestr+=("Release: ")# Start of line for release
        day = re.search(r'/[\d]{1,2}',self.__release)# Search for day
        year = re.search(r'/[\d]{4}',self.__release)# Search for year
        month = re.search(r'^[\d]{1,2}',self.__release)# Search for day
        
        day= day.group()# Converts day,month,year to strings
        year=  year.group()
        month = month.group()
        
        year=year.lstrip("/")# Removes / from the strings
        day = day.lstrip("/")
        
        # This allows for the convertion of the int of month to string
        def months(x):
           switcher= {
             1:"January",
             2:"February",
             3:"March",
             4:"April",
             5:"May",
             6:"June",
             7:"July",
             8:"August",
             9:"September",
             10:"October",
             11:"November",
             12:"December"
           }
           return switcher.get(x,"not a month")
        moviestr+=("{} {}, {}".format(months(int(month)), day,year)+"\n")
        return moviestr
    
    #This will return the value of title from a movie object
    def getTitle(self):
        return self.__title
    
    #This will return the value of genre from a movie object
    def getGenre(self):
        return self.__genre
    
    #This will return the value of director from a movie object
    def getDirector(self):
        return self.__director
    
    #This will return the value of writer from a movie object
    def getWriter(self):
        return self.__writer
    
    #This will return the value of all the stars from a movie object
    def getStars(self):
        stars = "{} {} {}".format(self.__star1, self.__star2, self.__star3)
        return stars
    
    #This will return the value of the run time from a movie object
    def getTime(self):
        return self.__runTime
    
    #This will return the value of rating from a movie object
    def getRating(self):
        return self.__rating
        
    #This will return the value of the release date from a movie object
    def getRelease(self):
        return self.__release