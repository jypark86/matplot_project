#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import time
from random import *

def main():

	vector_0 = []
	vector_1 = []
	vector_2 = []
	vector_3 = []
	vector_4 = []
	vector_5 = []
	vector_6 = []
	vector_7 = []
	vector_8 = []
	vector_9 = []

#	plt.ylim((0,100)

	file_1 = open("/home/vsi/python_sample_file/project_sample_1",'r')
	file_2 = open("/home/vsi/python_sample_file/result",'w')

	while 1:
#	for k in range(10):
		read_data = file_1.readline()
		if not read_data: break

		split_data=read_data.replace('=',',').replace(' \n','').split(",")	# data parsing
   
		for i in range(20):
			if(i%2 == 1):
#			print(split_data[i] + ",")
				file_2.write(split_data[i] + ",")
		file_2.write("\n")
	
	file_1.close()
	file_2.close()

	file_3 = open("/home/vsi/python_sample_file/result",'r')
		
	while 1:	# arrange column data
		read_data = file_3.readline()
		if not read_data: break

		split_data = read_data.split(",")

		vector_0.append(split_data[0])
		vector_1.append(split_data[1])
		vector_2.append(split_data[2])
		vector_3.append(split_data[3])
		vector_4.append(split_data[4])
		vector_5.append(split_data[5])
		vector_6.append(split_data[6])
		vector_7.append(split_data[7])
		vector_8.append(split_data[8])
		vector_9.append(split_data[9])
	
	index = [vector_0,vector_1,vector_2,vector_3,vector_4,vector_5,vector_6,vector_7,vector_8,vector_9]
	for i, name in enumerate(index):
		print(i, name)

	file_3.close()
#	plt.plot(new_vector_set)

#	plt.ion()
#	plt.show()
#	plt.pause(0.001)

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

#	plt.show(block=True)
#	time.sleep(1)

if __name__ == '__main__':
	main()
