class myClass(): # define a class that does depend on other classes
	def method1(self): # define a function/method inside the class depending on the object the method is operated on
		print "myClass method1"

	def method2(self, someString):
		print "myClass method2: " + someString

class anotherClass(myClass):
	def method2(self):
		print "anotherClass method2" # This is going to overwrite method2 called in the super class

	def method1(self):
		myClass.method1(self); # This is going to overwrite method1 called in the super class
		print "anotherClass method1"

def main():
	c = myClass()
	c.method1()
	c.method2("This is a string.")
	c2 = anotherClass()
	c2.method1()
	c2.method2()

if __name__ == "__main__":
	main()



# myClass method2: This is a string
# myClass method1
# anotherClass method1
# anotherClass method2