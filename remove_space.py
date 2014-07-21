import csv

newlist = []
with open("Temp_Fightvaw_data.csv","rU") as csvfile:
	reader=csv.reader(csvfile)
	for row in reader:
		print row , "ROW"
		row[3]=row[3].replace(", ",",")
		newlist.append(row)

print newlist
for row in newlist:
	for i in range(len(row)):
		if row[i] == "False":
			row[i] = "Unknown"
			print row

print newlist
with open ("Fightvaw_data.csv","wb") as f:
	writer = csv.writer(f)
	writer.writerows(newlist)