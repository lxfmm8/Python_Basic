import urllib2

def main():
	webUrl = urllib2.urlopen("http://lxfmm8.github.io")

	print "result code: " + str(webUrl.getcode())

	data = webUrl.read()
	print data

if __name__ == "__main__":
	main()