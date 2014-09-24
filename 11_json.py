import urllib2
import json

def printResults(data):
	theJSON = json.loads(data)
	if "title" in theJSON["metadata"]:
		print theJSON["metadata"]["title"]

	count = theJSON["metadata"]["count"];
	print str(count) + " events recorded"

	# for each event, print where it occured
	for i in theJSON["features"]:
		print i["properties"]["place"]

	# print only events that have a magnitute greater than 4
	for i in theJSON["features"]:
		if i["properties"]["mag"] >= 4.0:
			print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]

def main():

	urlData = "http://earthquakes.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

	webUrl = urllib2.urlopen(urlData)
	print webUrl.getcode()
	if (webUrl.getcode() == 200):
		data = webUrl.read()

		printResults(data)

if __name__ == "__main__":
	main()