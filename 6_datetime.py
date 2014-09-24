from datetime import date
from datetime import time
from datetime import datetime

def main():
	# today = date.today()
	# print "Today's date is ", today

	# print "Date Components: ", today.day, today.month, today.year

	# print "Today's Weekday #: ", today.weekday()

	today = datetime.now()
	# print "The current date and time is ", today;

	# t = datetime.time(datetime.now())
	# print "The currrent time is ", t

	wd = date.weekday(today) # weekday gives a number from 0-6

	days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
	print "Today is day number %d" % wd # %d is day number
	print "Which is a " + days[wd]

if __name__ == "__main__":
	main();