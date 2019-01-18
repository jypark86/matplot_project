#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import time
from random import *

def main():

#	vector_set = [[0]*10 for i in range(20)]
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
#			print(split_data[i] + ",")
				file_2.write(split_data[i] + " ")
		file_2.write("\n")
	
	file_1.close()
	file_2.close()

	file_3 = open("/home/vsi/python_sample_file/result",'r')
		
#	while 1:	# arrange column data
#		read_data = file_3.readline()
#		if not read_data: break
		
	vector_set = [read_data.split() for read_data in file_3]

#row in matrix
#	vector_row = []
#	for row in ragne(0,len(vector_set)):	#len(matrix)
#			vector_row.append(matrix[row])
#	print(vector_row)	# getting all of vector_row in list

#column in matrix
	vector_col=[]
	for row in zip(*vector_set):
			vector_col.append(row)
	print(vector_col)	# getting all of vector_col in list 

	plt.ylim(2100,2150)  
	plt.plot(vector_col[0], color='blue')
	plt.show()

### just check visually!
# 	print(vector_set)
#	index = [vector_col]
#	for i, name in enumerate(index):
#		print(i, name)
###
	
	file_3.close()
#	plt.ylim((0,5000))
	
#	vector_0[0]
#	plt.plot(vector_0[0], color='blue')
#	plt.plot(vector_1[0], color='red')
	
#	plt.ion()
#	plt.show()
#	plt.pause(0.001) # wait for drawding graph

	
#	for i in range(len(vector_0)):
		
#		plt.ylim((0,5000))
#		vector_0[i+1]
#		vector_1[i+1]
		
#		plt.clf()

#	draw graph to use vector_list, can use any color in RGB

#		plt.plot(vector_0[i+1], color='blue')
#		plt.plot(vector_1[i+1], color='green')
#		plt.plot(vector_2, color='red')
#		plt.plot(vector_3, color='cyan')
#		plt.plot(vector_4, color='magenta')
#		plt.plot(vector_5, color='yellow')
#		plt.plot(vector_6, color='black')
#		plt.plot(vector_7, color='white')
#		plt.plot(vector_8)
#		plt.plot(vector_9)
	
#		plt.ion()
#		plt.pause(0.001)
#		plt.show()
#		time.sleep(1)
#############################################################
#	for i in range(50):

#	read_data = file.readline()
#		new_read

#	for i in range(50):

#		plt.ylim((0,100))
#		k = randint(1,100)
#		vector_set.append(k)
#		new_vector_set = vector_set[i+1:i+11]
	
#		plt.clf()
#		plt.plot(new_vector_set)
	
#		plt.ion()
#		plt.pause(0.001)
#		plt.show()
############################################################	
#	plt.show(block=True)
	file_3.close()
#	time.sleep(1)

if __name__ == '__main__':
	main()
