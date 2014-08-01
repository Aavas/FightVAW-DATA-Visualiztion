import os , csv, random, string,json
import operator

def get_file_path(filename):
 	currentdirpath = os.getcwd()
 	file_path = os.path.join(os.getcwd(), filename)
 	print file_path
 	return file_path


path = get_file_path("../json_files/Fightvaw_data.csv")


def read_csv(filepath):
	year = {}
	i = 0
	with open(filepath, "rU") as csvfile:
		
		reader = csv.reader(csvfile)

		newspapers=[]
		for row in reader:
			print row
			if "Source" not in row[1]:
				

				if row[1] not in newspapers:
					newspapers.append(row[1])
					print newspapers

		totallist=[{}] # List of dictionaries
		
		csvfile=open(filepath,"rU")

		print csvfile
		reader = csv.reader(csvfile)


		j=0

		for row in reader:
			if "Date" not in row[0]:
				date=row[0].split('-')
				i=0
				found=False	

				while(i<len(totallist)):
					if date[0] in totallist[i].values():
						found=True
						break
					i=i+1
				if found==False:	
					totallist[j]["Year"]=date[0]
					for n in newspapers:
						totallist[j][n]=0
					totallist.append({})
					j=j+1
		print totallist ,"hello\n"

		csvfile=open(filepath,"rU")
		reader = csv.reader(csvfile)
		

		for row in reader:
			year=row[0].split("-")[0]
			i=0
			for currentdict in totallist[0:-1]:
				if year == currentdict["Year"]:
				 	currentdict[row[1]]=int(currentdict[row[1]])+1
				i=i+1

		
		jsonarray=[]
		for i in sorted(totallist[0:-1], key=operator.itemgetter("Year")):
			jsonarray.append(i)

		# for i in jsonarray:
		# 	for k , v in i.items():
		# 		if v == 0:
		# 			i.pop()


		source_list = json.dumps(jsonarray)
		print source_list , 'Hello'

	f = open("../json_files/codepython_output.json","w")

	f.write(source_list)
	f.close()

read_csv(path)
