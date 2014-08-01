import os , csv, random, string,json
import operator

def get_file_path(filename):
 	currentdirpath = os.getcwd()
 	file_path = os.path.join(os.getcwd(), filename)
 	print file_path
 	return file_path


path = get_file_path("../json_files/Fightvaw_data.csv")


def read_csv(filepath):

	month_dictionary = {'01':'Jan' ,'02':'Feb' ,'03':'Mar','04':'Apr','05':'May','06':'Jun' ,'07':'Jul' ,'08':'Aug' ,'09':'Sep' ,'10':'Oct' ,'11':'Nov' ,'12':'Dec'}
	

	def months_sort(mon):
		for key,value in month_dictionary.items():
			#print key , value
			#print mon["Month"] , 'check' , value
			if key == mon:
				return value


	year = {}
	with open(filepath, "rU") as csvfile:
		reader = csv.reader(csvfile)

		combo = []
		for row in reader:
			if "Date" not in row:

				years = row[0].split("-")[0]
				month = row[0].split("-")[1]

				#monthvalue = months_sort(month)

				file_name = [years, month] #list of all year and month combo
				if file_name not in combo:
					combo.append(file_name)


		print combo

	with open(filepath, "rU") as csvfile:
		reader = csv.reader(csvfile)

		for year_month in combo:
			print year_month , "Year , Month"


			csvfile=open(filepath,"rU")
			reader = csv.reader(csvfile)

			type_of_violence = []
			district = []

			for row in reader:
							
				if "Date" not in row:
					#print row
					
					years = row[0].split("-")[0]
					month = row[0].split("-")[1]
					
					if years==year_month[0] and month == year_month[1]:
						#print row[3]
						type_of_violence.append(row[3])
						district.append(row[2])

			# print type_of_violence
			# print district
			
			tov_count = {}
			for i in type_of_violence:
				for j in i.split(","):
					if j not in tov_count:
						tov_count[j] = 0
					tov_count[j] += 1
			#print tov_count

			# sorted_tov_count=[]
			# for i in sorted(tov_count, key=operator.itemgetter("TOV_Cases") , reverse = True):
			# 	sorted_tov_count.append(i)

			district_count = {}
			for i in district:
				if i not in district_count:
					district_count[i] = 0
				district_count[i] += 1
			#print district_count

			# sorted_district_count=[]
			# for i in sorted(district_count, key=operator.itemgetter("District_Cases") , reverse = True):
			# 	sorted_district_count.append(i)

			#dict_collection = sorted_tov_count,sorted_district_count
			dict_collection = tov_count,district_count

		
			if len(tov_count)>len(district_count):
				length = len(tov_count)
			else:
				length = len(district_count)

			print dict_collection , length

##############################################################################
			data_list = []

			for i in range(length):
				data_list.append({})

			i = 0
			for keys , values in tov_count.items():
				print keys, values
				data_list[i]["TOV"] = keys
				data_list[i]["TOV_Cases"] = values
				i += 1

			i=0
			for keys , values in district_count.items():
				print keys, values
				data_list[i]["District"] = keys
				data_list[i]["District_Cases"] = values
				i += 1

			for i in data_list:
				if len(i) == 2:
					if len(tov_count) > len(district_count):
						i["District_Cases"] = ""
					else:
						i["TOV_Cases"] = ""
				#print data_list

			donut_data = json.dumps(data_list)

			write_year = year_month[0]
			temp_month = year_month[1]
			write_month = months_sort(temp_month)

			f =open("../json_files/" +write_year+write_month+".json","w")
			f.write(donut_data)
			f.close


read_csv(path)
