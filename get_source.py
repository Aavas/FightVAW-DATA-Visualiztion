import csv
import urllib2
import json
req = urllib2.Request("http://fightvaw.org/snapshot/news")

opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())

print json

f = open("Temp_Fightvaw_data.csv", "wb")
writer = csv.writer(f)
writer.writerows(json)
