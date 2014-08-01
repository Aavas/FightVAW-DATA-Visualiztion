import os , csv, random, string,json
import datetime
import operator

def get_file_path(filename):
 	currentdirpath = os.getcwd()
 	file_path = os.path.join(os.getcwd(), filename)
 	print file_path
 	return file_path


path = get_file_path("../json_files/Fightvaw_data.csv")


def read_csv(filepath):
	#year = {}
	month_dictionary = {'01':'Jan' ,'02':'Feb' ,'03':'Mar','04':'Apr','05':'May','06':'Jun' ,'07':'Jul' ,'08':'Aug' ,'09':'Sep' ,'10':'Oct' ,'11':'Nov' ,'12':'Dec'}
	i = 0

	def months_sort(mon):
		for key,value in month_dictionary.items():
			#print key , value
			#print mon["Month"] , 'check' , value
			if value == mon["Month"]:
				return int(key)


	with open(filepath, "rU") as csvfile:
		reader = csv.reader(csvfile)

		newspapers=[]
		for row in reader:
			if "Source" not in row[1]:
				if row[1] not in newspapers:
					newspapers.append(row[1])
					print newspapers

		csvfile=open(filepath,"rU")
		reader = csv.reader(csvfile)

		all_years = []
		for row in reader:
			year=row[0].split("-")[0]
			if "Date" not in year:
				if year not in all_years:
					all_years.append(year)

		print all_years

		
		for year in all_years:
			print year
			
			totallist= [{}]
			j = 0
			print totallist , 'list must be empty'

			csvfile=open(filepath,"rU")
			reader = csv.reader(csvfile)
			
			for row in reader:
			 	if "Date" not in row:
				 	
				 	years=row[0].split("-")[0]
				 	month=row[0].split("-")[1]

				
					if year == years:
				 		
				 		########################
				 		i=0
				 		found=False	

						while(i<len(totallist)):
							if month in totallist[i].values():
								found=True
								break
							i=i+1
						if found==False:	
							totallist[j]["Month"]=month
							for n in newspapers:
								totallist[j][n]=0
							totallist.append({})
							j=j+1

						for currentdict in totallist[0:-1]:
							#print month , currentdict['Month']
							if month == currentdict["Month"]:
							 	currentdict[row[1]]=int(currentdict[row[1]])+1
								#print currentdict

						#print totallist[0:-1] , "totalist\n"


			
			for monthitem in totallist[0:-1]:
		 		try:
		 			monthitem["Month"] = month_dictionary[monthitem['Month']]
		 		except KeyError:
		 			print "already done"
		 
			month_list = json.dumps(sorted(totallist[:-1],key = months_sort))
						
			print month_list , 'new' , year
						# print years			
			f = open("../json_files/" + year + "test.json","w")
			f.write(month_list)
			f.close()

			
	
read_csv(path)