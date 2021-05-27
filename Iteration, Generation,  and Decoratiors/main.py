
# Use nbrValues as the number of values to generate for Exercises 1-5
nbrValues = int(input("What is the number of items you want to generate?\n"))

###############################################################
# Exercise 1 - Cubed Values from a Generator Object
###############################################################
print("%-16s" % "Cubes: ", end=' ')

class Iterator:
    def __init__(self,end):
        self.number = 1
        self.end = end
        
    def __iter__(self):
        return self
            
    def __next__(self):
        if self.number <= self.end:
            result = self.number * self.number * self.number 
            self.number+=1
            return result
        else:
            raise StopIteration
            
            
itt = Iterator(nbrValues)
for each in itt:
    print(end ="{} ".format(each))


print("")
###############################################################
# Exercise 2 - Prime Values from a Generator Object
###############################################################
print("\n%-16s" % "Primes: ", end=' ')
def isPrime(n):
        for i in range(2,n):
            if n%i==0:
                return False
        return True


class Iterator:
    
    def __init__(self,end):
        self.first = 2
        self.number = 0
        self.end = end
        
    def __iter__(self):
        return self
            
    def __next__(self):
        if self.number< self.end:
            while not isPrime(self.first):
                self.first += 1
            self.number+=1
            result= self.first
            self.first+=1
            return result
        else:
            raise StopIteration
            
itt = Iterator(nbrValues)
for each in itt:
    print(end ="{} ".format(each))


print("")
###############################################################
# Exercise 3 - Odd Negative Values from a Generator Function
###############################################################
print("\n%-16s" % "Odd Negatives: ", end=' ')

def genOdd(n):
    number = -1
    count= 0
    while  count < n:
            result =number
            yield result
            number-=2 
            count+=1
        
for each in genOdd(nbrValues):
    print(end ="{} ".format(each))

print("")
###############################################################
# Exercise 4 - Fibonacci Values from a Generator Function
###############################################################
print("\n%-16s" % "Fibonacci: ", end=' ')

def genFib(n):
    number = 1
    end = n
    currentNum = 0
    nextNum = 1
    results = 0 
    while number<= end:
            fib = currentNum +nextNum
            currentNum = nextNum
            yield currentNum
            nextNum = fib
            number+=1

for each in genFib(nbrValues):
    print(end ="{} ".format(each))

print("")
###############################################################
# Exercise 5 - Triangular Values from a Generator Expression
###############################################################
print("\n%-16s" % "Triangular: ", end=' ')

def genTri(n):
    number = 1
    while number <= n:
            result = int(number * (number+1)/2)
            yield result
            number+=1
            

for each in genTri(nbrValues):
    print(end ="{} ".format(each))
    
print("")
###############################################################
# Exercise 6 - Making Ice Cream with Decorators
###############################################################
print("\n%-16s" % "Ice Cream: ")

# TODO: Make this function a Decorator
def addBrownie(func):
	def wrapper():
	    print("Adding Brownie")
	    func()
	return wrapper
	    
# TODO: Make this function a Decorator
def addBanana(func):
    def wrapper():
        print("Adding Banana")
        func()
    return wrapper

# TODO: Make this function a Decorator
def addSyrup(func):
    def wrapper():
        func()
        print("Adding Chocolate Syrup")
    return wrapper
        
# TODO: Make this function a Decorator
def addNuts(func):
    def wrapper():
    	func()
    	print("Adding Nuts")
    return wrapper

# TODO: Make this function a Decorator
def addCherry(func):
    def wrapper():
        func()
        print("Adding the Cherry on Top!")
    return wrapper
        
@addBrownie
@addBanana
@addCherry
@addNuts
@addSyrup
# DO NOT MODIFY ANYTHING BELOW THIS LINE
def addIceCream():
	print("Adding Ice Cream")
	
addIceCream()
###############################################################
# Exercise 7 - Custom Toppings using Decorators and Arguments
###############################################################
print("\n%-16s" % "Custom Toppings: ")
    
# TODO: Implement a Decorator to add Base ingredients
def decor1(string):
    def outerWrapper(func):
        def wrapper(*args, **kwargs):
            print(string)
            action = func()
            return action
        return wrapper
    return outerWrapper
        
# TODO: Implement a Decorator to add Topping ingredients
def decor2(string):
    def outerWrapper(func):
        def wrapper(*args, **kwargs):
            action = func()
            print(string)
            return action
        return wrapper
    return outerWrapper
@decor1("Adding Brownie")
@decor1("Adding Banana")
@decor2( "Adding the Cherry on Top!")
@decor2( "Adding Nuts")
@decor2( "Adding Chocolate Syrup")
# DO NOT MODIFY ANYTHING BELOW THIS LINE
def addIceCream2():
	print("Adding Ice Cream")

addIceCream2()
