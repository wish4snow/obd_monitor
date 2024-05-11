import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import csv
import os

# os.chdir("sessions")

#csv processing, I did not make this
#this is from https://www.geeksforgeeks.org/working-csv-files-python/
#i didn't feel like making this myself lol

def plotter(file_name, wanted_user_pid_index):

	# initializing the titles and rows list
	fields = []
	rows = []
	
	# reading csv file
	with open(file_name, 'r') as csvfile:
	    # creating a csv reader object
	    csvreader = csv.reader(csvfile)

	    # extracting field names through first row
	    fields = next(csvreader)

	    # extracting each data row one by one
	    for row in csvreader:
	    	rows.append(row)
	
	count_rows = []
	value_rows = []
	name_rows = []

	for i in range(wanted_user_pid_index, len(rows), number_of_zeros(file_name)):

		count_rows.append(int(rows[i][0]))
		value_rows.append(float(rows[i][2]))
		name_rows.append(rows[i][1])
	# for row in range(len(rows)):
	
	plt.plot(count_rows, value_rows)
	plt.title(name_rows[0])
	# plt.legend(str("in " + same_value_rows[1]))
	plt.show()

def number_of_zeros(file_name) :
	
	file = open(file_name, 'r')
	count = 0

	for i in file:
		# print (str(file[:1]))
		if i[:1] == '1':
			return count

		count += 1

#plotter("session_data_2024-05-11 15:19:18.447936.csv", 2)


