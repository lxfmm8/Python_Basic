#Xiaofeng Lin
# Example file for HelloWorld
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

# Define function "main"
def main():
  print "Hello World"

# call function  "main"
if __name__ == "__main__":
  main()

# Python's built-in function "str"
print "Me too" + str(123)


# Global and Local Variables
f = 0
print f

def someFunction():
  global f
  f = "def"
  print f

someFunction()
print f # This section is going to print "0 def def".

# Delete variable that is previously delared.
del f
print f # This is going to cause an error.
