import os , csv, random, string,json
import datetime
import operator

def get_file_path(filename):
 	currentdirpath = os.getcwd()
 	file_path = os.path.join(os.getcwd(), filename)
 	print file_path
 	return file_path


path = get_file_path("Fightvaw_data.csv")


def read_csv(filepath):
	year = {}
	i = 0
	with open(filepath, "rU") as csvfile:
		reader = csv.reader(csvfile)

		district=[]
		for row in reader:
			if "District" not in row[2]:
				if row[2] not in district:
					district.append(row[2])
					print district


		csvfile=open(filepath,"rU")
		reader = csv.reader(csvfile)

		all_years = []
		for row in reader:
			year=row[0].split("-")[0]
			if "Date" not in year:
				if year not in all_years:
					all_years.append(year)

		print all_years

		
		j = 0
		totallist= [{}]
		for year in all_years:
			print year 

			csvfile=open(filepath,"rU")
			reader = csv.reader(csvfile)
			
			for row in reader:
			 	if "Date" not in row:
				 	date = row[0]

				 	new_date = datetime.datetime.strptime(date,"%Y-%m-%d")
					new_date = new_date.strftime("%b,%Y")

					splitter= new_date.split(",")
					month = splitter[0]
					years = splitter[1]
					dis_list = [{}]
					if year == years:
				 		totallist.append(row[2])
				 		
			print totallist , 'hello'
			

			counts = {}
			for new_district in totallist[1:]:
			 	if new_district not in counts:
			 		counts[new_district] = 0
			 	counts[new_district] +=1
			
			newlist = [{}]
			for district,cases in counts.items():
				newlist[0]["District"] = district
				newlist[0]["Cases"] = cases
				newlist.insert(0,{})
			print newlist[1:] , "Before sort"

			jsonarray=[]
			for i in sorted(newlist[1:], key=operator.itemgetter("Cases") , reverse = True):
				jsonarray.append(i)

			print jsonarray , "After sort"
			dumped_list = json.dumps(jsonarray[:10])
					
			f = open(year + "district.json","w")
			f.write(dumped_list)
			f.close()
			#print counts.keys() , ":" ,counts.values()

			totallist = [{}]
	
read_csv(path)