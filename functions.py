# Let's explore the function and how to write them
# #and also what they do 
 

def greeting():
	# say hello
	print("Hello from your first function!")


# This is how you call or invoke a function
greeting()


def greetings(msg="Hello there!", num=0):
	print("Our function say", msg, "The second arg is ", num)


greetings()
greetings("This is an argument", 1)	
greetings("Why we are arguing?", 2)	

myVariableNumber =0


def someMath(num1=2, num2=5):
global myVariable Number                                             

	myVariableNumber = num1 + num2
	return num1 + num2


sum = someMath()
print("Our sum variable is: ", sum, "myVariableNumber is also", num)