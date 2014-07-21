import os , csv, random, string,json
import operator

def get_file_path(filename):
 	currentdirpath = os.getcwd()
 	file_path = os.path.join(os.getcwd(), filename)
 	print file_path
 	return file_path


path = get_file_path("Fightvaw_data.csv")


def read_csv(filepath):

	


	year = {}
	with open(filepath, "rU") as csvfile:
		reader = csv.reader(csvfile)

		combo = []
		for row in reader:
			if "Date" not in row:

				years = row[0].split("-")[0]
				district = row[2]
				#monthvalue = months_sort(month)

				file_name = [years, district] #list of all year and month combo
				if file_name not in combo:
					combo.append(file_name)


		print combo

	with open(filepath, "rU") as csvfile:
		reader = csv.reader(csvfile)

		for year_district in combo:
			print year_district[0] , ":Year",year_district[1] , ":Dis"


			csvfile=open(filepath,"rU")
			reader = csv.reader(csvfile)

			type_of_violence = []

			for row in reader:
							
				if "Date" not in row:
					#print row
					
					years = row[0].split("-")[0]
					district = row[2]
					
					if years==year_district[0] and district == year_district[1]:
						print row[3]
						type_of_violence.append(row[3])

			#print type_of_violence
			
			tov_count = {}
			for i in type_of_violence:
				for j in i.split(","):
					if j not in tov_count:
						tov_count[j] = 0
					tov_count[j] += 1
			print tov_count
			print len(tov_count)

# 			district_count = {}
# 			for i in district:
# 				if i not in district_count:
# 					district_count[i] = 0
# 				district_count[i] += 1
# 			print district_count

# 			dict_collection = tov_count,district_count

			
# 			if len(tov_count)>len(district_count):
# 				length = len(tov_count)
# 			else:
# 				length = len(district_count)

# 			print dict_collection , length

# ##############################################################################
			data_list = []

			for i in range(len(tov_count)):
				data_list.append({})

			print data_list

			i = 0
			for keys , values in tov_count.items():
				#print keys, values
				data_list[i]["TOV"] = keys
				data_list[i]["TOV_Cases"] = values
				i += 1
			print data_list

# 			i=0
# 			for keys , values in district_count.items():
# 				print keys, values
# 				data_list[i]["District"] = keys
# 				data_list[i]["District_Cases"] = values
# 				i += 1

# 			for i in data_list:
# 				if len(i) == 2:
# 					if len(tov_count) > len(district_count):
# 						i["District_Cases"] = ""
# 					else:
# 						i["TOV_Cases"] = ""
# 				print data_list

			donut_data = json.dumps(data_list)

			write_year = year_district[0]
			write_district = year_district[1]

			f =open(write_year+write_district+".json","w")
			f.write(donut_data)
			f.close




				

					





		
		
########################################################################### Year ko month ko all type of violence nikalnu paryo
		# type_of_violence=[]
		# for row in reader:
		# 	if "Type_of_violence" not in row[3]:
		# 		# if row[3] not in type_of_violence:
		# 			type_of_violence.append(row[3])
		# print type_of_violence , "this is all of violence"
###########################################################################
		# csvfile=open(filepath,"rU")
		# reader = csv.reader(csvfile)

		# all_years = []
		# for row in reader:
		# 	year=row[0].split("-")[0]
		# 	if "Date" not in year:
		# 		if year not in all_years:
		# 			all_years.append(year)

		# print all_years

		# count = 0
		# for year in all_years: # yaha 4 choti loop lagcha cuz all_years ma 4 items
		# 	print year

		# 	this_new_list = [{}]
			
			

		# 	csvfile=open(filepath,"rU")
		# 	reader = csv.reader(csvfile)

			# for row in reader:
			# 	if "Type_of_violence" not in row:

			# 		years = row[0].split("-")[0]
			# 		month = row[0].split("-")[1]

			# 		monthvalue = months_sort(month)

			# 		file_name = years+monthvalue
					#print file_name

					# if year == years:
						
					# 	print year
					# 	a=0

						# count = {}
						# for i in type_of_violence:
						# 	for j in i.split(","):
						# 		if i not in count:
						# 			count[j] = 0
						# 		count[j] += 1
						# print count

						# csvfile=open(filepath,"rU")
						# reader = csv.reader(csvfile)

						# district = []
						# for row in reader:
						# 	if "District" not in row[2]:
						# 		district.append(row[2])
						# #print district

						# count2 = {}
						# for i in district:
						# 	if i not in count2:
						# 		count2[i] = 0
						# 	count2[i] += 1
						# #print count2


						# dict_collection = count, count2
						# if len(count)>len(count2):
						# 	length = len(count)
						# else:
						# 	length = len(count2)

						# # print len(count) , len(count2)
						# # print length
						# # print dict_collection

						# data_list = []

						# for i in range(length):
						# 	data_list.append({})

						# i = 0
						# for keys , values in count.items():
						# 	#print keys, values
						# 	data_list[i]["TOV"] = keys
						# 	data_list[i]["TOV_Cases"] = values
						# 	i += 1

						# i=0
						# for keys , values in count2.items():
						# 	#print keys, values
						# 	data_list[i]["District"] = keys
						# 	data_list[i]["District_Cases"] = values
						# 	i += 1

						# for i in data_list:
						# 	if len(i) == 2:
						# 		if len(count) > len(count2):
						# 			i["District_Cases"] = ""
						# 		else:
						# 			i["TOV_Cases"] = ""

					#print year
					

					#donut_data = json.dumps(data_list)

					# f = open(file_name+".json","w")
					# f.write(file_name)
					# f.close



			# f = open("type_of_violence.csv", "w")
			# f.write("Type_of_violence,Cases")

			# writer_tov = csv.writer(open("donut_tov.csv","wb"))
			# writer_tov.writerow(["Type_of_violence","Cases"])
			# for key , value in count.items():
			#  	writer_tov.writerow([key,value])

			# writer_dis = csv.writer(open("donut_dis.csv","wb"))
			# writer_dis.writerow(["District","Cases1"])
			# for key , value in count2.items():
			#  	writer_dis.writerow([key,value])


read_csv(path)
