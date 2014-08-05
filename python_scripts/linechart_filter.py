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
	year = {}
	i = 0
	with open(filepath, "rU") as csvfile:
		reader = csv.reader(csvfile)

		Source=[]
		for row in reader:
			if "Source" not in row[1]:
				if row[1] not in Source:
					Source.append(row[1])
		print Source

		for sources in Source:
			
			csvfile=open(filepath,"rU")
			reader = csv.reader(csvfile)

			day_list = []

			for row in reader:
				if "Source" not in row[1]:
					if sources==row[1]:
						day_list.append(row[0])
			#print day_list

			linechart_data = {}

			for day in day_list:
				if day not in linechart_data:
					linechart_data[day] = 0
				linechart_data[day] += 1

			#print linechart_data , 'Dict'

			write_data = sorted(linechart_data.items())

			writer = csv.writer(open("../json_files/"+sources+".csv","wb"))
			writer.writerow(["Day","Cases"])
			writer.writerows(write_data)
	
read_csv(path)