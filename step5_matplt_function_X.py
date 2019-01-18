#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import time
from random import *

def main():

	vector_set = []

	file_1 = open("/home/vsi/python_sample_file/project_sample_1",'r')
	file_2 = open("/home/vsi/python_sample_file/result",'w')

#	while 1:
	for k in range(20):
		read_data = file_1.readline()
		if not read_data: break

		split_data = read_data.replace('=',',').replace(' \n','').split(",")	# data parsing
   
		for i in range(20):
			if(i%2 == 1):
				file_2.write(split_data[i] + " ")
		file_2.write("\n")
	
	file_1.close()
	file_2.close()

### make matrix ###
	file_3 = open("/home/vsi/python_sample_file/result",'r')
		
	vector_set = [read_data.split() for read_data in file_3]

# row in matrix
#	vector_row = []
#	for row in ragne(0,len(vector_set)):	#len(matrix)
#			vector_row.append(matrix[row])
#	print(vector_row)	# getting all of vector_row in list

# column in matrix
	vector_col=[]
	for row in zip(*vector_set):
			vector_col.append(row)
#	print(vector_col)	# getting all of vector_col in list 

### draw graph ###
	fig = plt.figure()	
	row_start = 0
	row_end = 10
	
	new_vector_data = vector_col[0][row_start:row_end]
#	print(new_vector_data)
	
	plt.ylim(2100,2150)  
	plt.xlim(0,9)

	plt.plot(new_vector_data, color='blue')
	plt.ion()
	plt.show()
	plt.pause(0.001)
	plt.clf()

	j=1
	for j in range(10):

		new_vector_data= vector_col[0][row_start+j:row_end+j]
#		print(new_vector_data)

		plt.ylim(2100,2150)	
		plt.xlim(0,9)

		plt.plot(new_vector_data, color='red')
		plt.ion()
		plt.show()
		plt.pause(0.001)
		time.sleep(1)
		plt.clf()
	
	plt.show(block=True)
	file_3.close()

if __name__ == '__main__':
	main()
