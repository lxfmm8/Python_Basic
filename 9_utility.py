import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
	print os.name

	print "Item's path: " + str(path.realpath("textfile.txt"))
	print "Item's path and name: " + str(path.split(path.realpath("textfile.txt")))

	# Get modification time
	t = time.ctime(path.getmtime("textfile.txt"))
	print t
	print datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))

	#Calculate how long ago the item was modified
	td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
	print "It has been " + str(td) + " since the file was modified."
	print "Or, " + str(td.total_seconds()) + " seconds."

if __name__ == "__main__":
	main()