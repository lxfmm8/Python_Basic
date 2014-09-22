def main():
	x = 0
	# define a while loop
	# while (x < 5):
	# 	print x
	# 	x = x + 1
	
	#define a for loop
	# for x in  range(5, 10):
	# 	print x

	#use a for loop over a collection
	# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
	# for d in days:
	# 	print d
	for i, d in enumerate(days):
		print i, d # This is going to print both index number and their values

	# use the break and continue statements
	for x in range(5, 10);
		# if (x == 7): break # Terminate the loop
		if (x % 2 == 0): continue
		print x # This is going to skip even numbers

if __name__ == "__main__":
	main()