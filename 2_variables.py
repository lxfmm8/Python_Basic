# define a function
def func1():
  print "I am a function."

# function that takes arguments
def func2(arg1, arg2):
	print arg1, " ", arg2

# function with deafult value for an argument
def power(num, x=1):
	result = 1;
	for i in range(x):
		result = result * num
	return result

print power(x=3, num=2)

# function with variable number of arguments
def multi_add(*args):
	result = 0;
	for x in args:
		result = result + x
	return result

print multi_add(4, 5, 10, 4) # This is going to print 23